import React, { useEffect, useRef, useState } from 'react';
import { Timeline } from 'vis-timeline/standalone';
import 'vis-timeline/styles/vis-timeline-graph2d.min.css';
// import Graph2D from './graph';
// import Sidebar from './sidebar';
// import Graph2Dstorage from './graphstorage';
import './Schedular.css';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  TextField,
  Button,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';
import ItemPopup from './ItemPopup';

const Schedular = () => {
  const timelineRef = useRef(null);

  // React states
  const [items, setItems] = useState([]);
  const [modalOpen, setModalOpen] = useState(false);
  const [newTaskStart, setNewTaskStart] = useState('');
  const [commands, setCommands] = useState([]);
  const [selectedCommand, setSelectedCommand] = useState(null);
  const [selectedCommandId, setSelectedCommandId] = useState(null);

  const [nameDialogOpen, setNameDialogOpen] = useState(false);
  const [scheduleName, setScheduleName] = useState('');

  const [noteStartTime, setNoteStartTime] = useState(null);
  const [noteEndTime, setNoteEndTime] = useState(null);

  const [editableStartTime, setEditableStartTime] = useState('');
  const [timeChanged, setTimeChanged] = useState(false);

  // Popup states
  const [clickedItemStartTime, setClickedItemStartTime] = useState(null);
  const [isItemPopupOpen, setIsItemPopupOpen] = useState(false);
  const [selectedItemId, setSelectedItemId] = useState(null);

  // Timeline groups
  const groups = [
    {
      id: 'group1',
      content: 'Keeping',
      style: 'background-color: rgba(255, 192, 203, 0.5)',
    },
    {
      id: 'group2',
      content: 'Astrodynamics',
      style: 'background-color: rgba(0, 256, 0, 1)',
    },
    {
      id: 'group3',
      content: 'Imagning',
      style: 'background-color: rgba(0, 0, 265, 0.5)',
    },
  ];

  // --------------------
  // 1) Fetch Existing Data & Commands
  // --------------------
  useEffect(() => {
    // Fetch the schedule data
    fetch('http://127.0.0.1:8000/api/schedule-planner/schedule-sets/3/')
      .then((response) => response.json())
      .then((data) => {
        const formattedItems = data.schedules.map((item) => {
          // Convert item.start_time to a string with no trailing 'Z'
          const startString = item.time_tag.replace('Z', '');
          // Convert end time similarly:
          // item.duration in seconds => item.start_time + duration
          const endDate = new Date(
            new Date(item.time_tag).getTime() + item.duration * 1000
          );
          const endString = endDate.toISOString().split('.')[0].replace('Z', '');

          return {
            id: item.id,
            start: startString,
            end: endString,
            content: `Command ${item.command}`,
            group: 'group2',
            command: item.command,
          };
        });
        setItems(formattedItems);
      })
      .catch((error) => console.error('Error fetching schedule data:', error));

    // Fetch the list of commands
    fetch('http://127.0.0.1:8000/telemetry/commnands/')
      .then((response) => response.json())
      .then((data) => setCommands(data))
      .catch((error) => console.error('Error fetching commands:', error));
  }, []);

  // --------------------
  // 2) Initialize / Update Timeline
  // --------------------
  useEffect(() => {
    const options = {
      editable: {
        add: false,
        updateTime: true,
        updateGroup: false,
        remove: true,
        overrideItems: false,
      },
      selectable: true,
      stack: true,
      groups: groups,
      minHeight: 500,
      maxHeight: 500,
      height: '100%',
      width: '90%',
      onUpdate: (item, callback) => {
        setItems((prevItems) =>
          prevItems.map((i) => (i.id === item.id ? item : i))
        );
        callback(item);
      },
      onMove: (item, callback) => {
        setItems((prevItems) =>
          prevItems.map((i) => (i.id === item.id ? item : i))
        );
        callback(item);
      },
      onMoving: (item, callback) => {
        setItems((prevItems) =>
          prevItems.map((i) => (i.id === item.id ? item : i))
        );
        callback(item);
      },
    };

    if (timelineRef.current && items.length > 0) {
      let currentTimeline = timelineRef.current.timeline;

      if (!currentTimeline) {
        const newTimeline = new Timeline(
          timelineRef.current,
          items,
          options,
          groups
        );
        timelineRef.current.timeline = newTimeline;

        newTimeline.on('rangechange', (event) => {
          if (event) {
            setNoteStartTime(event.start.toISOString());
            setNoteEndTime(event.end.toISOString());
          } else {
            console.warn("Warning: 'range' property is undefined in 'rangechange' event.");
          }
        });

        // Attach a basic move listener to update items.
        newTimeline.on('move', (event) => {
          setItems((prevItems) =>
            prevItems.map((i) =>
              i.id === event.item
                ? { ...i, start: event.start, end: event.end }
                : i
            )
          );
        });
      } else {
        currentTimeline.setItems(items);
        currentTimeline.setOptions(options);
        currentTimeline.setGroups(groups);
      }
    }
  }, [items, groups]);

  // --------------------
  // 3) Attach "Double Click" Listener using the LATEST items
  // --------------------
  useEffect(() => {
    if (!timelineRef.current || !timelineRef.current.timeline) return;

    const currentTimeline = timelineRef.current.timeline;
    currentTimeline.off('doubleClick');

    currentTimeline.on('doubleClick', (props) => {
      const clickedItemId = props.item;
      if (!clickedItemId) return;

      const foundItem = items.find(
        (i) => String(i.id) === String(clickedItemId)
      );
      if (foundItem) {
        // Store the selected item's id
        setSelectedItemId(foundItem.id);
        // Set the clicked item's start time (convert Date if needed)
        if (
          foundItem.start &&
          typeof foundItem.start.toISOString === 'function'
        ) {
          setClickedItemStartTime(
            foundItem.start.toISOString().split('.')[0].replace('Z', '')
          );
        } else {
          setClickedItemStartTime(foundItem.start);
        }
        setIsItemPopupOpen(true);
      }
    });
  }, [items]);

// --------------------
// 4) Update Popup Start Time When User Slides (Moves) the Item
// --------------------
useEffect(() => {
  const timeline = timelineRef.current?.timeline;
  if (!timeline) return;

  const onMoving = (event) => {
    if (isItemPopupOpen && selectedItemId && event.item === selectedItemId) {
      // Format the new start time as an ISO string without trailing 'Z'
      const newStartString = new Date(event.start)
        .toISOString()
        .split('.')[0]
        .replace('Z', '');
      setClickedItemStartTime(newStartString);
    }
  };

  timeline.on('moving', onMoving);
  return () => {
    timeline.off('moving', onMoving);
  };
}, [isItemPopupOpen, selectedItemId]);


  // --------------------
  // 5) Add New Item Logic
  // --------------------
  const addItem = () => {
    if (timelineRef.current && timelineRef.current.timeline) {
      const middleTimeDate = new Date(
        (timelineRef.current.timeline.getWindow().start.getTime() +
          timelineRef.current.timeline.getWindow().end.getTime()) /
          2
      );
      const middleTimeString = middleTimeDate
        .toISOString()
        .split('.')[0]
        .replace('Z', '');
      setEditableStartTime(middleTimeString);
      setNewTaskStart(middleTimeString);
    }
    setModalOpen(true);
  };

  const saveNewItem = () => {
    if (selectedCommand && newTaskStart.trim()) {
      const parsedStart = new Date(newTaskStart);
      const parsedEnd = new Date(parsedStart.getTime() + 36000);
      const startString = parsedStart
        .toISOString()
        .split('.')[0]
        .replace('Z', '');
      const endString = parsedEnd
        .toISOString()
        .split('.')[0]
        .replace('Z', '');
      const newId = Math.max(0, ...items.map((item) => item.id)) + 1;
      const newItem = {
        id: newId,
        content: selectedCommand.name,
        start: startString,
        end: endString,
        group: 'group1',
        command: selectedCommandId,
      };
      setItems([...items, newItem]);
      if (timelineRef.current?.timeline) {
        timelineRef.current.timeline.itemsData.add(newItem);
      }
      setModalOpen(false);
      setSelectedCommand(null);
      setSelectedCommandId(null);
    }
  };

  // --------------------
  // 6) Saving to DB
  // --------------------
  const saveToDB = (name) => {
    const formattedItems = items.map((item) => ({
      start_time: item.start,
      duration: (new Date(item.end) - new Date(item.start)) / 1000,
      parameters: null,
      onBoardStatus: '',
      command: item.command,
    }));

    const requestPayload = {
      name: name,
      status: 'Draft',
      schedule: formattedItems,
    };

    fetch('http://127.0.0.1:8000/api/schedule-sets/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(requestPayload),
    })
      .then((response) => response.json())
      .then((data) => console.log('Saved successfully:', data))
      .catch((error) => console.error('Error saving schedule:', error));
  };

  // --------------------
  // 7) Handlers for the Command Selection & Name
  // --------------------
  const handleCommandSelect = (command) => {
    setSelectedCommand(command);
    setSelectedCommandId(command.id);
  };

  const handleNameChange = (e) => {
    setScheduleName(e.target.value);
  };

  const handleNameSubmit = () => {
    if (scheduleName.trim()) {
      saveToDB(scheduleName);
      setNameDialogOpen(false);
    }
  };

  // --------------------
  // 8) Zoom Timeline Handler
  // --------------------
  const zoomTimeline = (hours) => {
    if (timelineRef.current && timelineRef.current.timeline) {
      const timeline = timelineRef.current.timeline;
      const { start, end } = timeline.getWindow();
      const center = new Date((start.getTime() + end.getTime()) / 2);
      const halfDuration = (hours * 60 * 60 * 1000) / 2;
      const newStart = new Date(center.getTime() - halfDuration);
      const newEnd = new Date(center.getTime() + halfDuration);

      timeline.setWindow(newStart, newEnd, {
        animation: { duration: 500, easingFunction: 'easeInOutQuad' },
      });
    }
  };

  // --------------------
  // 9) Render
  // --------------------
  return (
    <div className="app">
      <h1 style={{ marginLeft: '366px' }}>
        Mission Drishti Master Timeline
      </h1>
      {/* <Sidebar /> */}

      {/* Timeline container */}
      <div ref={timelineRef} style={{ width: '86%', marginLeft: '366px' }} />

      {/* Zoom controls */}
      <div
        className="zoom-controls"
        style={{
          marginLeft: '366px',
          marginTop: '10px',
          display: 'flex',
          gap: '10px',
        }}
      >
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(1)}
        >
          1 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(2)}
        >
          2 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(3)}
        >
          3 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(4)}
        >
          4 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(5)}
        >
          5 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(6)}
        >
          6 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(7)}
        >
          7 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(8)}
        >
          8 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(9)}
        >
          9 Hour View
        </Button>
        <Button
          variant="contained"
          color="primary"
          onClick={() => zoomTimeline(10)}
        >
          10 Hour View
        </Button>
      </div>

      {/* Buttons row */}
      <div className="controls" style={{ marginLeft: '366px' }}>
        <Button variant="contained" color="primary" onClick={addItem}>
          Add Item
        </Button>
        <Button
          variant="contained"
          color="secondary"
          onClick={() => setNameDialogOpen(true)}
        >
          Save to DB
        </Button>
      </div>

      {/* Popup for item click */}
      <ItemPopup
        open={isItemPopupOpen}
        startTime={clickedItemStartTime}
        onClose={() => setIsItemPopupOpen(false)}
      />

      {/* Graphs */}
      {/* <Graph2D
        noteStartTime={noteStartTime}
        noteEndTime={noteEndTime}
        items={items}
      /> */}
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      {/* <Graph2Dstorage noteStartTime={noteStartTime} noteEndTime={noteEndTime} /> */}

      {/* Dialog for selecting a command */}
      <Dialog open={modalOpen} onClose={() => setModalOpen(false)}>
        <DialogTitle>Select Command</DialogTitle>
        <DialogContent>
          <TextField
            label="Start Time (optional)"
            type="datetime-local"
            value={timeChanged ? newTaskStart : editableStartTime}
            onChange={(e) => {
              setNewTaskStart(e.target.value);
              setTimeChanged(true);
            }}
            fullWidth
          />

          <List>
            {commands.map((command) => (
              <ListItem
                button
                key={command.id}
                onClick={() => handleCommandSelect(command)}
                style={{
                  backgroundColor:
                    selectedCommandId === command.id ? '#2c3e50' : 'transparent',
                  color:
                    selectedCommandId === command.id ? '#fff' : 'inherit',
                }}
              >
                <ListItemText
                  primary={command.name}
                  secondary={command.description}
                />
              </ListItem>
            ))}
          </List>

          <Button
            variant="contained"
            color="primary"
            onClick={saveNewItem}
            style={{ marginTop: '10px' }}
          >
            Save
          </Button>
        </DialogContent>
      </Dialog>

      {/* Dialog for entering schedule name */}
      <Dialog open={nameDialogOpen} onClose={() => setNameDialogOpen(false)}>
        <DialogTitle>Enter Schedule Name</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            label="Schedule Name"
            value={scheduleName}
            onChange={handleNameChange}
          />
          <Button
            variant="contained"
            color="primary"
            onClick={handleNameSubmit}
            style={{ marginTop: '10px' }}
          >
            Save
          </Button>
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default Schedular;
