import React, { useState } from 'react';
import './SatelliteTaskCreator.css';

// Custom DateTime picker with millisecond precision
const DateTimeMsPicker = ({ label, value, onChange }) => {
  // Parse initial value or default to current date/time
  const initialDate = value ? new Date(value) : new Date();
  const [date, setDate] = useState(initialDate.toISOString().slice(0, 10)); // YYYY-MM-DD
  const [hours, setHours] = useState(initialDate.getHours());
  const [minutes, setMinutes] = useState(initialDate.getMinutes());
  const [seconds, setSeconds] = useState(initialDate.getSeconds());
  const [milliseconds, setMilliseconds] = useState(initialDate.getMilliseconds());

  // Combine all fields into one ISO string and propagate upward
  const updateDateTime = (newDate, newHours, newMinutes, newSeconds, newMilliseconds) => {
    const [year, month, day] = newDate.split('-');
    const combined = new Date(year, month - 1, day, newHours, newMinutes, newSeconds, newMilliseconds);
    onChange(combined.toISOString());
  };

  const handleDateChange = (e) => {
    setDate(e.target.value);
    updateDateTime(e.target.value, hours, minutes, seconds, milliseconds);
  };
  const handleHoursChange = (e) => {
    const h = parseInt(e.target.value, 10);
    setHours(h);
    updateDateTime(date, h, minutes, seconds, milliseconds);
  };
  const handleMinutesChange = (e) => {
    const m = parseInt(e.target.value, 10);
    setMinutes(m);
    updateDateTime(date, hours, m, seconds, milliseconds);
  };
  const handleSecondsChange = (e) => {
    const s = parseInt(e.target.value, 10);
    setSeconds(s);
    updateDateTime(date, hours, minutes, s, milliseconds);
  };
  const handleMillisecondsChange = (e) => {
    const ms = parseInt(e.target.value, 10);
    setMilliseconds(ms);
    updateDateTime(date, hours, minutes, seconds, ms);
  };

  return (
    <div className="datetime-picker form-group">
      <label className="form-label">{label}</label>
      <div className="datetime-inputs">
        <input 
          type="date" 
          value={date} 
          onChange={handleDateChange} 
          className="form-input date-input"
        />
        <input 
          type="number" 
          value={hours} 
          onChange={handleHoursChange} 
          min="0" max="23" 
          className="form-input time-input"
          placeholder="HH"
        />
        <input 
          type="number" 
          value={minutes} 
          onChange={handleMinutesChange} 
          min="0" max="59" 
          className="form-input time-input"
          placeholder="MM"
        />
        <input 
          type="number" 
          value={seconds} 
          onChange={handleSecondsChange} 
          min="0" max="59" 
          className="form-input time-input"
          placeholder="SS"
        />
        <input 
          type="number" 
          value={milliseconds} 
          onChange={handleMillisecondsChange} 
          min="0" max="999" 
          className="form-input time-input"
          placeholder="MS"
        />
      </div>
    </div>
  );
};

// Ten satellite-inspired command templates with fixed command_id "613"
const commandTemplates = [
  {
    id: 'template1',
    name: 'ADCS Launch Sequence',
    commands: [
      { time_offset: 100, parameters: { action: "ADCS_take_off" }, command_id: "613" },
      { time_offset: 200, parameters: { action: "MSI_initialize" }, command_id: "613" },
      { time_offset: 300, parameters: { action: "Storage_allocate" }, command_id: "613" },
      { time_offset: 400, parameters: { action: "Refresh_cycle" }, command_id: "613" }
    ]
  },
  {
    id: 'template2',
    name: 'Orbital Adjustment',
    commands: [
      { time_offset: 110, parameters: { action: "ADCS_adjust" }, command_id: "613" },
      { time_offset: 210, parameters: { action: "MSI_calibrate" }, command_id: "613" },
      { time_offset: 310, parameters: { action: "Storage_backup" }, command_id: "613" },
      { time_offset: 410, parameters: { action: "Refresh_comms" }, command_id: "613" }
    ]
  },
  {
    id: 'template3',
    name: 'Stability Check',
    commands: [
      { time_offset: 120, parameters: { action: "ADCS_stabilize" }, command_id: "613" },
      { time_offset: 220, parameters: { action: "MSI_verify" }, command_id: "613" },
      { time_offset: 320, parameters: { action: "Storage_inspect" }, command_id: "613" },
      { time_offset: 420, parameters: { action: "Refresh_diagnostics" }, command_id: "613" }
    ]
  },
  {
    id: 'template4',
    name: 'Deep Space Maneuver',
    commands: [
      { time_offset: 130, parameters: { action: "ADCS_maneuver" }, command_id: "613" },
      { time_offset: 230, parameters: { action: "MSI_optimize" }, command_id: "613" },
      { time_offset: 330, parameters: { action: "Storage_expand" }, command_id: "613" },
      { time_offset: 430, parameters: { action: "Refresh_sync" }, command_id: "613" }
    ]
  },
  {
    id: 'template5',
    name: 'Lunar Approach',
    commands: [
      { time_offset: 140, parameters: { action: "ADCS_align" }, command_id: "613" },
      { time_offset: 240, parameters: { action: "MSI_check" }, command_id: "613" },
      { time_offset: 340, parameters: { action: "Storage_prepare" }, command_id: "613" },
      { time_offset: 440, parameters: { action: "Refresh_link" }, command_id: "613" }
    ]
  },
  {
    id: 'template6',
    name: 'Solar Array Optimization',
    commands: [
      { time_offset: 150, parameters: { action: "ADCS_orient" }, command_id: "613" },
      { time_offset: 250, parameters: { action: "MSI_monitor" }, command_id: "613" },
      { time_offset: 350, parameters: { action: "Storage_secure" }, command_id: "613" },
      { time_offset: 450, parameters: { action: "Refresh_update" }, command_id: "613" }
    ]
  },
  {
    id: 'template7',
    name: 'Emergency Protocol',
    commands: [
      { time_offset: 160, parameters: { action: "ADCS_emergency" }, command_id: "613" },
      { time_offset: 260, parameters: { action: "MSI_shutdown" }, command_id: "613" },
      { time_offset: 360, parameters: { action: "Storage_lockdown" }, command_id: "613" },
      { time_offset: 460, parameters: { action: "Refresh_reset" }, command_id: "613" }
    ]
  },
  {
    id: 'template8',
    name: 'Orbit Correction',
    commands: [
      { time_offset: 170, parameters: { action: "ADCS_correct" }, command_id: "613" },
      { time_offset: 270, parameters: { action: "MSI_realign" }, command_id: "613" },
      { time_offset: 370, parameters: { action: "Storage_optimize" }, command_id: "613" },
      { time_offset: 470, parameters: { action: "Refresh_reboot" }, command_id: "613" }
    ]
  },
  {
    id: 'template9',
    name: 'Communication Boost',
    commands: [
      { time_offset: 180, parameters: { action: "ADCS_signal" }, command_id: "613" },
      { time_offset: 280, parameters: { action: "MSI_transmit" }, command_id: "613" },
      { time_offset: 380, parameters: { action: "Storage_archive" }, command_id: "613" },
      { time_offset: 480, parameters: { action: "Refresh_transmit" }, command_id: "613" }
    ]
  },
  {
    id: 'template10',
    name: 'System Diagnostics',
    commands: [
      { time_offset: 190, parameters: { action: "ADCS_diagnose" }, command_id: "613" },
      { time_offset: 290, parameters: { action: "MSI_analyze" }, command_id: "613" },
      { time_offset: 390, parameters: { action: "Storage_scan" }, command_id: "613" },
      { time_offset: 490, parameters: { action: "Refresh_self_check" }, command_id: "613" }
    ]
  },
];

const SatelliteTaskCreator = () => {
  // Form state for date/time ISO strings
  const [startTime, setStartTime] = useState(new Date().toISOString());
  const [endTime, setEndTime] = useState(new Date().toISOString());
  const [taskName, setTaskName] = useState('');
  const [priority, setPriority] = useState('1');
  const [category, setCategory] = useState('Imagning');
  const [selectedTemplate, setSelectedTemplate] = useState(commandTemplates[0].id);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Calculate duration in minutes from ISO strings
    const startDate = new Date(startTime);
    const endDate = new Date(endTime);
    const duration = Math.round((endDate - startDate) / 60000);

    // Get selected command template
    const template = commandTemplates.find(t => t.id === selectedTemplate);

    const payload = {
      task_name_optional: taskName,
      priority: parseInt(priority, 10),
      category,
      status: "Pending",
      duration,
      time_slots: [
        {
          start: startDate.toISOString(),
          end: endDate.toISOString()
        }
      ],
      task_commands: template.commands,
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/api/task-planner/tasks/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!response.ok) throw new Error('Network error');
      const data = await response.json();
      alert('Task created successfully!');
      console.log(data);
    } catch (error) {
      console.error('Error posting task:', error);
      alert('Failed to create task');
    }
  };

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <DateTimeMsPicker label="Start Time:" value={startTime} onChange={setStartTime} />
      <DateTimeMsPicker label="End Time:" value={endTime} onChange={setEndTime} />

      <div className="form-group">
        <label className="form-label">Task Name (optional):</label>
        <input
          type="text"
          className="form-input"
          value={taskName}
          onChange={(e) => setTaskName(e.target.value)}
          placeholder="Enter task name"
        />
      </div>

      <div className="form-group">
        <label className="form-label">Priority:</label>
        <select className="form-select" value={priority} onChange={(e) => setPriority(e.target.value)}>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Category:</label>
        <select className="form-select" value={category} onChange={(e) => setCategory(e.target.value)}>
          <option value="Imagning">Imagning</option>
          <option value="Housekeeping">Housekeeping</option>
          <option value="Astrodynamics">Astrodynamics</option>
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Command Template:</label>
        <select className="form-select" value={selectedTemplate} onChange={(e) => setSelectedTemplate(e.target.value)}>
          {commandTemplates.map(template => (
            <option key={template.id} value={template.id}>{template.name}</option>
          ))}
        </select>
      </div>

      <button type="submit" className="form-button">Create Task</button>
    </form>
  );
};

export default SatelliteTaskCreator;
