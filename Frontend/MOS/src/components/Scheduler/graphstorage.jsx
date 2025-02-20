import React, { useState, useEffect, useRef } from 'react';
import * as vis from 'vis';

const Graph2Dstorage = ({ noteStartTime, noteEndTime }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    const options = {
      start: noteStartTime ? new Date(noteStartTime).toISOString() : null,
      end: noteEndTime ? new Date(noteEndTime).toISOString() : null,
      zoomable: true,
      moveable: false,
      // Add this line to set the line color
      //lineColor: 'red',
    };

    const groupData = {
      id: 0,
      content: "Group Name",
      options: {
        drawPoints: {
          style: "square", // square, circle
        },
        shaded: {
          orientation: "zero", // top, bottom
        },

        eft: {
            lineColor: 'red'
          }
      },
    };

    const groups = new vis.DataSet();
    groups.add(groupData);

    const items = [



      { x: "2024-12-17T00:00:00", y: 0, group: 0 },
      { x: "2024-12-17T00:45:00", y: 0, group: 0 },
      { x: "2024-12-17T01:30:00", y: 0, group: 0 },
      { x: "2024-12-17T02:15:00", y: 0, group: 0 },
      { x: "2024-12-17T03:00:00", y: 0, group: 0 },
      { x: "2024-12-17T03:45:00", y: 0, group: 0 },
      { x: "2024-12-17T04:30:00", y: 0, group: 0 },
      { x: "2024-12-17T05:15:00", y: 0, group: 0 },
      { x: "2024-12-17T06:00:00", y: 0, group: 0 },
      { x: "2024-12-17T06:45:00", y: 0, group: 0 },
      { x: "2024-12-17T07:30:00", y: 0, group: 0 },
      { x: "2024-12-17T08:15:00", y: 0, group: 0 },
      { x: "2024-12-17T09:00:00", y: 0, group: 0 },
      { x: "2024-12-17T09:45:00", y: 0, group: 0 },
      { x: "2024-12-17T10:30:00", y: 0, group: 0 },
      { x: "2024-12-17T11:15:00", y: 0, group: 0 },

      //{ id: 531, content: 'Project F', start: '2024-12-17T11:48:45', end: '2024-12-17T11:51:45', group: 'group2', style: 'background-color: rgba(0, 0, 265, 1)' },
      //{ id: 5301, content: 'Project F', start: '2024-12-17T11:38:45', end: '2024-12-17T11:41:45', group: 'group1', style: 'background-color: rgba(255, 192, 203, 1)' },
      //{ id: 53001, content: 'Project F', start: '2024-12-17T11:18:45', end: '2024-12-17T11:21:45', group: 'group3', style: 'background-color: rgba(0, 256, 0, 1)' },
      
      { x: "2024-12-17T12:00:00", y: 600, group: 0 },

      


      { x: "2024-12-17T12:45:00", y: 600, group: 0 },

      //{ id: 53005, content: 'Project G', start: '2024-12-17T12:11:45', end: '2024-12-17T12:16:45', group: 'group3', style: 'background-color: rgba(0, 256, 0)'  },
      //{ id: 532, content: 'Project G', start: '2024-12-17T12:48:45', end: '2024-12-17T12:51:45', group: 'group2', style: 'background-color: rgba(0, 0, 265, 1)'  },
      //{ id: 536, content: 'Project H', start: '2024-12-17T13:03:45', end: '2024-12-17T13:08:45', group: 'group2', style: 'background-color: rgba(0, 0, 265, 1)'  },


      { x: "2024-12-17T13:30:00", y: 1300, group: 0 },



      //{ id: 53006, content: 'Project H', start: '2024-12-17T13:07:45', end: '2024-12-17T13:13:45', group: 'group3', style: 'background-color: rgba(0, 256, 0)'  },
      //{ id: 5306, content: 'Project H', start: '2024-12-17T13:33:45', end: '2024-12-17T13:38:45', group: 'group1', style: 'background-color: rgba(255, 192, 203)'  },
      //{ id: 53004, content: 'Project F', start: '2024-12-17T14:01:45', end: '2024-12-17T14:06:45', group: 'group3', style: 'background-color: rgba(0, 256, 0)' },
      //{ id: 5305, content: 'Project G', start: '2024-12-17T14:11:45', end: '2024-12-17T14:16:45', group: 'group1', style: 'background-color: rgba(255, 192, 203)'  },


      { x: "2024-12-17T14:15:00", y: 1900, group: 0 },



      //{ id: 535, content: 'Project G', start: '2024-12-17T14:31:45', end: '2024-12-17T14:36:45', group: 'group2', style: 'background-color: rgba(0, 0, 265, 1)'  },
      //{ id: 53002, content: 'Project G', start: '2024-12-17T15:19:45', end: '2024-12-17T15:21:45', group: 'group3', style: 'background-color: rgba(0, 256, 0)'  },


      { x: "2024-12-17T15:00:00", y: 2200, group: 0 },

      //{ id: 534, content: 'Project F', start: '2024-12-17T15:01:45', end: '2024-12-17T15:06:45', group: 'group2', style: 'background-color: rgba(0, 0, 265, 1)' },


      { x: "2024-12-17T15:45:00", y: 2300, group: 0 },

      //{ id: 5302, content: 'Project G', start: '2024-12-17T15:48:45', end: '2024-12-17T15:51:45', group: 'group1', style: 'background-color: rgba(255, 192, 203)'  },
      //{ id: 5304, content: 'Project F', start: '2024-12-17T16:01:45', end: '2024-12-17T16:06:45', group: 'group1', style: 'background-color: rgba(255, 192, 203)' },
      //{ id: 5303, content: 'Project H', start: '2024-12-17T16:18:45', end: '2024-12-17T16:21:45', group: 'group1', style: 'background-color: rgba(255, 192, 203)'  },



      { x: "2024-12-17T16:30:00", y: 2900, group: 0 },


      { x: "2024-12-17T17:15:00", y: 0, group: 0 },

      //{ id: 533, content: 'Project H', start: '2024-12-17T15:48:45', end: '2024-12-17T15:51:45', group: 'group2', style: 'background-color: rgba(0, 0, 265, 1)'  },
      //{ id: 53003, content: 'Project H', start: '2024-12-17T17:28:45', end: '2024-12-17T17:31:45', group: 'group3', style: 'background-color: rgba(0, 256, 0)'  },


      { x: "2024-12-17T18:00:00", y: 500, group: 0 },


      { x: "2024-12-17T18:45:00", y: 700, group: 0 },


      { x: "2024-12-17T19:30:00", y: 1100, group: 0 },


      { x: "2024-12-17T20:15:00", y: 1300, group: 0 },


      { x: "2024-12-17T21:00:00", y: 1450, group: 0 },


      { x: "2024-12-17T21:45:00", y: 700, group: 0 },


      { x: "2024-12-17T22:30:00", y: 1500, group: 0 },


      { x: "2024-12-17T23:15:00", y: 2000, group: 0 },
      { x: "2024-12-18T00:00:00", y: 2100, group: 0 },
      { x: "2024-12-18T00:45:00", y: 0, group: 0 },
      { x: "2024-12-18T01:30:00", y: 0, group: 0 },
      { x: "2024-12-18T02:15:00", y: 0, group: 0 },
      { x: "2024-12-18T03:00:00", y: 0, group: 0 },
      { x: "2024-12-18T03:45:00", y: 0, group: 0 },
      { x: "2024-12-18T04:30:00", y: 0, group: 0 },
      { x: "2024-12-18T05:15:00", y: 0, group: 0 },
      { x: "2024-12-18T06:00:00", y: 0, group: 0 },
      { x: "2024-12-18T06:45:00", y: 0, group: 0 },
      { x: "2024-12-18T07:30:00", y: 0, group: 0 },
      { x: "2024-12-18T08:15:00", y: 0, group: 0 },
      { x: "2024-12-18T09:00:00", y: 0, group: 0 },
      { x: "2024-12-18T09:45:00", y: 0, group: 0 },
      { x: "2024-12-18T10:30:00", y: 0, group: 0 },
      { x: "2024-12-18T11:15:00", y: 0, group: 0 },
      { x: "2024-12-18T12:00:00", y: 0, group: 0 },
      { x: "2024-12-18T12:45:00", y: 0, group: 0 },
      { x: "2024-12-18T13:30:00", y: 0, group: 0 },
      { x: "2024-12-18T14:15:00", y: 0, group: 0 },
      { x: "2024-12-18T15:00:00", y: 0, group: 0 },
      { x: "2024-12-18T15:45:00", y: 0, group: 0 },
      { x: "2024-12-18T16:30:00", y: 0, group: 0 },
      { x: "2024-12-18T17:15:00", y: 0, group: 0 },
      { x: "2024-12-18T18:00:00", y: 0, group: 0 },
      { x: "2024-12-18T18:45:00", y: 0, group: 0 },
      { x: "2024-12-18T19:30:00", y: 0, group: 0 },
      { x: "2024-12-18T20:15:00", y: 0, group: 0 },
      { x: "2024-12-18T21:00:00", y: 0, group: 0 },
      { x: "2024-12-18T21:45:00", y: 0, group: 0 },
      { x: "2024-12-18T22:30:00", y: 0, group: 0 },
      { x: "2024-12-18T23:15:00", y: 0, group: 0 },

      { x: "2024-12-19T00:00:00", y: 0, group: 0 },
      { x: "2024-12-19T00:45:00", y: 0, group: 0 },
      { x: "2024-12-19T01:30:00", y: 0, group: 0 },
      { x: "2024-12-19T02:15:00", y: 0, group: 0 },
      { x: "2024-12-19T03:00:00", y: 0, group: 0 },
      { x: "2024-12-19T03:45:00", y: 0, group: 0 },
      { x: "2024-12-19T04:30:00", y: 0, group: 0 },
      { x: "2024-12-19T05:15:00", y: 0, group: 0 },
      { x: "2024-12-19T06:00:00", y: 0, group: 0 },
      { x: "2024-12-19T06:45:00", y: 0, group: 0 },
      { x: "2024-12-19T07:30:00", y: 0, group: 0 },
      { x: "2024-12-19T08:15:00", y: 0, group: 0 },
      { x: "2024-12-19T09:00:00", y: 0, group: 0 },
      { x: "2024-12-19T09:45:00", y: 0, group: 0 },
      { x: "2024-12-19T10:30:00", y: 0, group: 0 },
      { x: "2024-12-19T11:15:00", y: 0, group: 0 },
      { x: "2024-12-19T12:00:00", y: 0, group: 0 },
      { x: "2024-12-19T12:45:00", y: 0, group: 0 },
      { x: "2024-12-19T13:30:00", y: 0, group: 0 },
      { x: "2024-12-19T14:15:00", y: 0, group: 0 },
      { x: "2024-12-19T15:00:00", y: 0, group: 0 },
      { x: "2024-12-19T15:45:00", y: 0, group: 0 },
      { x: "2024-12-19T16:30:00", y: 0, group: 0 },
      { x: "2024-12-19T17:15:00", y: 0, group: 0 },
      { x: "2024-12-19T18:00:00", y: 0, group: 0 },
      { x: "2024-12-19T18:45:00", y: 0, group: 0 },
      { x: "2024-12-19T19:30:00", y: 0, group: 0 },
      { x: "2024-12-19T20:15:00", y: 0, group: 0 },
      { x: "2024-12-19T21:00:00", y: 0, group: 0 },
      { x: "2024-12-19T21:45:00", y: 0, group: 0 },
      { x: "2024-12-19T22:30:00", y: 0, group: 0 },
      { x: "2024-12-19T23:15:00", y: 0, group: 0 },

    ];

    const dataset = new vis.DataSet(items);

    const graph2d = new vis.Graph2d(containerRef.current, dataset, groups, options);

    return () => {
      graph2d.destroy();
    };
  }, [noteStartTime, noteEndTime]); // Re-render on startTime and endTime changes

  return (
    <div style={{  }}>

      <div ref={containerRef} style={{ height: '300px', width: '78%', marginLeft: '366px' }} />
    </div>
  );
};

export default Graph2Dstorage;