<template>
  <div class="container">
    <table>
      <thead>
      <th>id</th>
      <th>todo</th>
      <th>assignee</th>
      <th>done</th>
      </thead>
      <tbody>
      <tr v-for="todo in todos">
        <td v-text="todo.id"></td>
        <td v-text="todo.todo"></td>
        <td v-text="todo.assignee"></td>
        <td v-text="todo.done"></td>
      </tr>
      </tbody>
    </table>

    <div>
      <h1>Create</h1>
      <input type="text" id="createTodo">
      <input type="text" id="createAssignee">
      <input type="text" id="createDone">
      <input type="Button" v-on:click="addTodo()">
    </div>

    <div>
      <h1>Update</h1>
      <input type="text" id="updateID">
      <input type="text" id="updateTodo">
      <input type="text" id="updateAssignee">
      <input type="text" id="updateDone">
      <input type="Button" v-on:click="updateTodo()">
    </div>

    <div>
      <h1>Delete</h1>
      <input type="text" id="deleteID">
      <input type="Button" v-on:click="removeTodo()">
    </div>
  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    data() {
      return {
        todos: []
      };
    },
    methods: {
      getTodos() {
        const path = 'http://localhost:8080/todos';
        axios.get(path)
          .then((res) => {
            this.todos = res.data.todos;
            console.log(this.todos)
          })
          .catch((error) => {
            console.error(error);
          });
      },
      addTodo() {
        const path = 'http://localhost:8080/todos';
        const payload = {
          todo: document.getElementById('createTodo').value,
          assignee: document.getElementById('createAssignee').value,
          done: document.getElementById('createDone').value
        };
        axios.post(path, payload)
          .then(() => {
            this.getTodos();
            this.message = 'Todo added!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getTodos();
          });
      },
      updateTodo() {
        const payload = {
          todo: document.getElementById('updateTodo').value,
          assignee: document.getElementById('updateAssignee').value,
          done: document.getElementById('updateDone').value
        };
        var todoID = document.getElementById('updateID');
        const path = `http://localhost:8080/todos/${todoID}`;
        axios.put(path, payload)
          .then(() => {
            this.getTodos();
            this.message = 'Todo updated!';
            this.showMessage = true;
          })
          .catch((error) => {
            console.error(error);
            this.getTodos();
          });
      },
      removeTodo() {
        var todoID = document.getElementById('deleteID').value;
        const path = `http://localhost:8080/todos/${todoID}`;
        axios.delete(path)
          .then(() => {
            this.getTodos();
          })
          .catch((error) => {
            console.error(error);
            this.getTodos();
          });
      }
    },
    created() {
      this.getTodos();
    },
  };
</script>
