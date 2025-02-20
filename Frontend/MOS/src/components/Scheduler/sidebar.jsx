import React, { useState } from 'react';
import {
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Collapse,
  styled,
  Button,
} from '@mui/material';
import {
  Inbox as InboxIcon,
  Drafts as DraftsIcon,
  Send as SendIcon,
  ExpandMore as ExpandMoreIcon,
  Archive as ArchiveIcon,  // New icon for Archiving
  Folder as FolderIcon,    // New icon for Sub-Items
} from '@mui/icons-material';

// Styled Drawer for custom styling
const StyledDrawer = styled(Drawer)(({ theme }) => ({
  '& .MuiDrawer-paper': {
    width: 240,
    backgroundColor: theme.palette.background.paper, // Better contrast
    color: theme.palette.text.primary,
    position: 'fixed', // Make the drawer fixed
    top: 0,
    left: 0,
    zIndex: 1000, // Ensure it's on top of other elements
    boxShadow: theme.shadows[5], // Add subtle shadow for better depth
  },
}));

const Sidebar = () => {
  const [openImportNewOrders, setOpenImportNewOrders] = useState(false);
  const [importNewOrders, setImportNewOrders] = useState([
    'Ritesh',
    'Rahul',
    'Sumesh',
    'Nitesh',
    'Vinita',
    'Madhunika',
    'Ragha',
  ]);
  const [openImportProjects, setOpenImportProjects] = useState(false);
  const [importProjects, setImportProjects] = useState([
    'Project Berlin',
    'Global Fishing Watch',
    'DRDO',
  ]);
  const [openImportHousekeepingSchedule, setOpenImportHousekeepingSchedule] = useState(false);
  const [importHousekeepingSchedule, setImportHousekeepingSchedule] = useState([
    'Momentum Dumping',
    'Software Update',
    'Camera Calibration',
  ]);
  const [openImportManeuverSchedule, setOpenImportManeuverSchedule] = useState(false);
  const [importManeuverSchedule, setImportManeuverSchedule] = useState([
    'Achieve Orbital Tube',
    'Collision Avoidance',
    'Raise Orbit',
  ]);

  const [openArchiving, setOpenArchiving] = useState(false);  // State for archiving

  // Handling clicks to toggle menu items
  const handleImportNewOrdersClick = () => {
    setOpenImportNewOrders(!openImportNewOrders);
  };

  const handleImportProjectsClick = () => {
    setOpenImportProjects(!openImportProjects);
  };

  const handleImportHousekeepingScheduleClick = () => {
    setOpenImportHousekeepingSchedule(!openImportHousekeepingSchedule);
  };

  const handleImportManeuverScheduleClick = () => {
    setOpenImportManeuverSchedule(!openImportManeuverSchedule);
  };

  const handleArchivingClick = () => {
    setOpenArchiving(!openArchiving);  // Toggle archiving menu
  };

  const handleImportItem = (list, setList) => {
    setList((prevList) => prevList.slice(1)); // Remove the first item from the list
  };

  return (
    <StyledDrawer variant="permanent" anchor="left" open>
      <h2>Task Queue</h2>
      <List>
        {/* Import New Orders Section */}
        <ListItem button onClick={handleImportNewOrdersClick}>
          <ListItemIcon>
            <InboxIcon />
          </ListItemIcon>
          <ListItemText primary="Import New Orders" />
          {openImportNewOrders ? <ExpandMoreIcon /> : <></>}
        </ListItem>
        <Collapse in={openImportNewOrders} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {importNewOrders.map((order, index) => (
              <ListItem key={index} button>
                <ListItemText primary={order} />
                <Button onClick={() => handleImportItem(importNewOrders, setImportNewOrders)}>
                  Import
                </Button>
              </ListItem>
            ))}
          </List>
        </Collapse>

        {/* Import Projects Section */}
        <ListItem button onClick={handleImportProjectsClick}>
          <ListItemIcon>
            <DraftsIcon />
          </ListItemIcon>
          <ListItemText primary="Import Projects" />
          {openImportProjects ? <ExpandMoreIcon /> : <></>}
        </ListItem>
        <Collapse in={openImportProjects} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {importProjects.map((project, index) => (
              <ListItem key={index} button>
                <ListItemText primary={project} />
                <Button onClick={() => handleImportItem(importProjects, setImportProjects)}>
                  Import
                </Button>
              </ListItem>
            ))}
          </List>
        </Collapse>

        {/* Import Housekeeping Schedule Section */}
        <ListItem button onClick={handleImportHousekeepingScheduleClick}>
          <ListItemIcon>
            <SendIcon />
          </ListItemIcon>
          <ListItemText primary="Import Housekeeping Schedule" />
          {openImportHousekeepingSchedule ? <ExpandMoreIcon /> : <></>}
        </ListItem>
        <Collapse in={openImportHousekeepingSchedule} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {importHousekeepingSchedule.map((schedule, index) => (
              <ListItem key={index} button>
                <ListItemText primary={schedule} />
                <Button onClick={() => handleImportItem(importHousekeepingSchedule, setImportHousekeepingSchedule)}>
                  Import
                </Button>
              </ListItem>
            ))}
          </List>
        </Collapse>

        {/* Import Maneuver Schedule Section */}
        <ListItem button onClick={handleImportManeuverScheduleClick}>
          <ListItemIcon>
            <ExpandMoreIcon />
          </ListItemIcon>
          <ListItemText primary="Import Maneuver Schedule" />
          {openImportManeuverSchedule ? <ExpandMoreIcon /> : <></>}
        </ListItem>
        <Collapse in={openImportManeuverSchedule} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {importManeuverSchedule.map((schedule, index) => (
              <ListItem key={index} button>
                <ListItemText primary={schedule} />
                <Button onClick={() => handleImportItem(importManeuverSchedule, setImportManeuverSchedule)}>
                  Import
                </Button>
              </ListItem>
            ))}
          </List>
        </Collapse>

        {/* Archiving Section */}
        <ListItem button onClick={handleArchivingClick}>
          <ListItemIcon>
            <ArchiveIcon /> {/* Archiving Icon */}
          </ListItemIcon>
          <ListItemText primary="Archiving" />
          {openArchiving ? <ExpandMoreIcon /> : <></>}
        </ListItem>
        <Collapse in={openArchiving} timeout="auto" unmountOnExit>
          <List component="div" disablePadding>
            {/* Archiving Sub-Items */}
            <ListItem button>
              <ListItemIcon>
                <FolderIcon />
              </ListItemIcon>
              <ListItemText primary="Archived Orders" />
            </ListItem>
            <ListItem button>
              <ListItemIcon>
                <FolderIcon />
              </ListItemIcon>
              <ListItemText primary="Archived Projects" />
            </ListItem>
            <ListItem button>
              <ListItemIcon>
                <FolderIcon />
              </ListItemIcon>
              <ListItemText primary="Archived Schedules" />
            </ListItem>
          </List>
        </Collapse>
      </List>
    </StyledDrawer>
  );
};

export default Sidebar;
