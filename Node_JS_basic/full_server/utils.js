import fs from 'fs';

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const fields = {};

    for (const student of students) {
      const studentData = student.split(',');
      if (studentData.length >= 4) {
        const firstName = studentData[0];
        const field = studentData[3].trim();
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }
    }
    resolve(fields);
  });
});

export default readDatabase;
