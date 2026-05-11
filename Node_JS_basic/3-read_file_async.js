const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      if (lines.length <= 1) {
        console.log('Number of students: 0');
        resolve();
        return;
      }
      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);
      const fields = {};

      for (const student of students) {
        const studentData = student.split(',');
        if (studentData >= 4) {
          const firstName = studentData[0];
          const field = studentData[3];
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstName);
        }
      }
      for (const [field, list] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
      resolve();
    });
  });
}
module.exports = countStudents;
