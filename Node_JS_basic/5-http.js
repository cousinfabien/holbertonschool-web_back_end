const http = require('http');
const fs = require('fs');

const DB_FILE = process.argv[2];

/**
 * Logique de lecture de fichier adaptée pour le serveur HTTP
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      if (lines.length <= 1) {
        resolve('Number of students: 0');
        return;
      }

      const students = lines.slice(1);
      let output = `Number of students: ${students.length}`;

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

      for (const [field, list] of Object.entries(fields)) {
        output += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
      }
      resolve(output);
    });
  });
}

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const data = await countStudents(DB_FILE);
      res.end(data);
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
