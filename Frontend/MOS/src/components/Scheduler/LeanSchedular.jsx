import React, { useState } from 'react';
import axios from 'axios';
import './TaskScheduler.css';

const TaskScheduler = () => {
  // Filters & States
  const [startTime, setStartTime] = useState('');
  const [endTime, setEndTime] = useState('');
  const [status, setStatus] = useState('Pending');
  const [category, setCategory] = useState('Imagning');
  const [priority, setPriority] = useState('0');

  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [scheduleDescription, setScheduleDescription] = useState('My Schedule Set');

  // States for optimization
  const [optimizing, setOptimizing] = useState(false);
  const [optimized, setOptimized] = useState(false);

  // Fetch tasks using filters
  const fetchTasks = async () => {
    try {
      setLoading(true);
      setError('');
      setOptimized(false);

      const baseUrl = 'http://127.0.0.1:8000/api/task-planner/tasks/';
      const params = new URLSearchParams();
      if (startTime) params.append('start_time', new Date(startTime).toISOString());
      if (endTime) params.append('end_time', new Date(endTime).toISOString());
      if (status) params.append('status', status);
      if (category) params.append('category', category);
      if (priority) params.append('priority', priority);

      const url = `${baseUrl}?${params.toString()}`;
      const res = await axios.get(url);

      const fetchedTasks = res.data.map((task) => {
        let defaultTime = '';
        if (task.time_slots && task.time_slots.length > 0) {
          defaultTime = task.time_slots[0].start;
        }
        return { ...task, selectedExecutionTime: defaultTime };
      });

      setTasks(fetchedTasks);
    } catch (err) {
      console.error(err);
      setError('Error fetching tasks. Check console for details.');
    } finally {
      setLoading(false);
    }
  };

  // Delete a task locally
  const handleDeleteTask = (taskId) => {
    setTasks((prev) => prev.filter((t) => t.id !== taskId));
  };

  // Update execution time of a task
  const handleTimeChange = (taskId, newTime) => {
    setTasks((prev) =>
      prev.map((t) => (t.id === taskId ? { ...t, selectedExecutionTime: newTime } : t))
    );
  };

  // Post remaining tasks as schedule
  const createSchedule = async () => {
    try {
      setLoading(true);
      setError('');

      const schedulesPayload = tasks.map((t) => ({
        task: t.id,
        execution_time: t.selectedExecutionTime,
      }));

      const payload = {
        description: scheduleDescription,
        schedules: schedulesPayload,
      };

      console.log('POSTing payload:', payload);
      const url = 'http://127.0.0.1:8000/api/schedule-planner/schedule-sets/';
      await axios.post(url, payload);
      alert('Schedule created successfully!');
    } catch (err) {
      console.error(err);
      setError('Error creating schedule. Check console for details.');
    } finally {
      setLoading(false);
    }
  };

  // Astroflow Optimiser: Simulate optimization for 3 seconds
  const handleOptimize = () => {
    setOptimizing(true);
    setOptimized(false);

    // Simulate a 3-second optimization process
    setTimeout(() => {
      setTasks((prev) =>
        prev.map((task) => {
          if (task.time_slots && task.time_slots.length > 0) {
            const randomSlotIndex = Math.floor(Math.random() * task.time_slots.length);
            const randomSlot = task.time_slots[randomSlotIndex];
            return { ...task, selectedExecutionTime: randomSlot.start };
          }
          return task;
        })
      );
      setOptimizing(false);
      setOptimized(true);
    }, 3000);
  };

  return (
    <div className="container">
      {/* Filter Section */}
      <div className="box">
        <h2 className="heading">1) Load tasks by filter</h2>
        <div style={{ marginBottom: '8px' }}>
          <label className="label">Start Time:</label>
          <input
            type="datetime-local"
            value={startTime}
            onChange={(e) => setStartTime(e.target.value)}
            className="input"
          />
          <label className="label">End Time:</label>
          <input
            type="datetime-local"
            value={endTime}
            onChange={(e) => setEndTime(e.target.value)}
            className="input"
          />
        </div>
        <div style={{ marginBottom: '8px' }}>
          <label className="label">Status:</label>
          <select value={status} onChange={(e) => setStatus(e.target.value)} className="select">
            <option value="">None</option>
            <option value="Pending">Pending</option>
            <option value="Staged">Staged</option>
            <option value="Send">Send</option>
            <option value="Executed">Executed</option>
            <option value="Failed">Failed</option>
          </select>
          <label className="label">Category:</label>
          <select value={category} onChange={(e) => setCategory(e.target.value)} className="select">
            <option value="">None</option>
            <option value="Imagning">Imagning</option>
            <option value="Maneouvring">Maneouvring</option>
            <option value="Housekeeping">Housekeeping</option>
          </select>
          <label className="label">Priority:</label>
          <select value={priority} onChange={(e) => setPriority(e.target.value)} className="select">
            <option value="">None</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
          </select>
          <button onClick={fetchTasks} disabled={loading} className="button">
            {loading ? 'Loading...' : 'Fetch Tasks'}
          </button>
        </div>
        {error && <div style={{ color: 'red', marginBottom: '10px' }}>{error}</div>}
      </div>

      {/* Tasks Table Section */}
      <div className="box">
        <h2 className="heading">2) Edit / Delete Tasks</h2>
        {tasks.length === 0 ? (
          <p>No tasks to display</p>
        ) : (
          <div className="table-container">
            <table className="table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Task Name</th>
                  <th>Priority</th>
                  <th>Category</th>
                  <th>Status</th>
                  <th>Duration</th>
                  <th>Time Slots</th>
                  <th>Execution Time (Editable)</th>
                  <th>Delete</th>
                </tr>
              </thead>
              <tbody>
                {tasks.map((task) => (
                  <tr key={task.id}>
                    <td>{task.id}</td>
                    <td>{task.task_name_optional || '---'}</td>
                    <td>{task.priority}</td>
                    <td>{task.category}</td>
                    <td>{task.status}</td>
                    <td>{task.duration}</td>
                    <td>
                      {task.time_slots && task.time_slots.length > 0 ? (
                        task.time_slots.map((ts) => (
                          <div key={ts.id}>
                            <strong>Start:</strong> {ts.start} <br />
                            <strong>End:</strong> {ts.end}
                          </div>
                        ))
                      ) : (
                        '---'
                      )}
                    </td>
                    <td>
                      <input
                        type="datetime-local"
                        value={
                          task.selectedExecutionTime
                            ? new Date(task.selectedExecutionTime).toISOString().slice(0, 16)
                            : ''
                        }
                        onChange={(e) => handleTimeChange(task.id, e.target.value)}
                        className="input"
                      />
                    </td>
                    <td>
                      <button onClick={() => handleDeleteTask(task.id)} className="button">
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Optimiser Section */}
      <div className="box">
        <h2 className="heading">Astroflow Optimiser</h2>
        <button onClick={handleOptimize} className="button big-button">
          Astroflow Optimiser
        </button>
        {optimizing && (
          <div style={{ textAlign: 'center', marginTop: '10px' }}>
            <div className="spinner"></div>
            <p>Optimizing...</p>
          </div>
        )}
        {!optimizing && optimized && (
          <div style={{ textAlign: 'center', marginTop: '10px' }}>
            <p>Schedule Optimized!</p>
          </div>
        )}
      </div>

      {/* Schedule Creation Section */}
      <div className="box">
        <h2 className="heading">3) Schedule Creation</h2>
        <div style={{ marginBottom: '8px' }}>
          <label className="label">Schedule Description:</label>
          <input
            type="text"
            value={scheduleDescription}
            onChange={(e) => setScheduleDescription(e.target.value)}
            className="input"
          />
        </div>
        <button
          onClick={createSchedule}
          disabled={loading || tasks.length === 0}
          className="button"
        >
          {loading ? 'Posting...' : 'Create Schedule with Remaining Tasks'}
        </button>
      </div>
    </div>
  );
};

export default TaskScheduler;
