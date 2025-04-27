const API_URL = '/api/tasks';



// Fetch tasks from the backend API
async function fetchTasks() {
  const response = await fetch('http://localhost:3000/tasks');
  const tasks = await response.json();
  const taskList = document.getElementById('task-list');
  taskList.innerHTML = '';  // Clear any existing tasks

  tasks.forEach(task => {
    const listItem = document.createElement('li');
    listItem.classList.add('task-item');

    // Add conditional class for completed or not completed task
    if (task.completed) {
      listItem.classList.add('completed');
    } else {
      listItem.classList.add('not-completed');
    }

    const taskText = document.createElement('span');
    taskText.textContent = `${task.title} - ${task.completed ? 'Completed' : 'Not Completed'}`;
    listItem.appendChild(taskText);

    // Create a delete button for each task
    const deleteButton = document.createElement('button');
    deleteButton.classList.add('delete-btn');
    deleteButton.textContent = 'Delete';
    deleteButton.onclick = () => deleteTask(task._id); // Pass the task ID to delete
    listItem.appendChild(deleteButton);

    // Append the list item to the task list
    taskList.appendChild(listItem);
  });
}

// Handle form submission to create a new task
document.getElementById('task-form').addEventListener('submit', async (e) => {
  e.preventDefault();  // Prevent form submission

  const taskTitle = document.getElementById('task-title').value;
  const taskCompleted = document.getElementById('task-completed').checked;

  const newTask = { title: taskTitle, completed: taskCompleted };

  // Send the new task to the backend
  await fetch('http://localhost:3000/tasks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newTask)
  });

  // Refresh the task list
  fetchTasks();

  // Clear the form fields
  document.getElementById('task-title').value = '';
  document.getElementById('task-completed').checked = false;
});

// Delete a task by ID
async function deleteTask(taskId) {
  // Send a DELETE request to the backend API to remove the task
  await fetch(`http://localhost:3000/tasks/${taskId}`, {
    method: 'DELETE',
  });

  // Refresh the task list after deletion
  fetchTasks();
}

// Initial fetch when the page loads
window.onload = fetchTasks;
