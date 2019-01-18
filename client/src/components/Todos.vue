<template>
  <div>
    <h1>VueJS-Client</h1>
    <div>
      <h3>Create</h3>
      <input type="text" id="createTodo" placeholder="todo">
      <input type="text" id="createAssignee" placeholder="assignee">
      <input type="text" id="createDone" placeholder="done">
      <input type="Button" id="postButton" v-on:click="addTodo()" value="Create">
    </div>

    <div>
      <h3>Update</h3>
      <input type="text" id="updateID" placeholder="ID">
      <input type="text" id="updateTodo" placeholder="Todo">
      <input type="text" id="updateAssignee" placeholder="assignee">
      <input type="text" id="updateDone" placeholder="done">
      <input type="Button" id="updateButton" v-on:click="updateTodo()" value="Update">
    </div>

    <div>
      <h3>Delete</h3>
      <input type="text" id="deleteID" placeholder="ID">
      <input type="Button" v-on:click="removeTodo()" value="Delete">
    </div>

    <div style="border-bottom: solid" v-for="t in todos">
        ID: {{ t.id}}<br>
        todo: {{ t.todo}}<br>
        assignee: {{ t.assignee}}<br>
        done: {{ t.done}
    </div>
  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    username: 'Client',
    data() {
      return {
        todos: []
      };
    },
    methods: {
      getTodos: function() {
        axios.get("http://localhost:8080/todos").then((res) => {
            this.todos = res.data;
            console.log(this.todos)
          }).catch((error) => {
            console.error(error);
          });
      },
      addTodo() {
        const payload = {
          todo: document.getElementById('createTodo').value,
          assignee: document.getElementById('createAssignee').value,
          done: document.getElementById('createDone').value
        };
        axios.post('http://localhost:8080/todos', payload)
          .then(() => {
            this.getTodos();
            this.message = 'Todo added!';
            this.showMessage = true;
          }).catch((error) => {
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
        axios.put('http://localhost:8080/todos/${todoID}', payload).then(() => {
            this.getTodos();
            this.message = 'Todo updated!';
            this.showMessage = true;
          }).catch((error) => {
            console.error(error);
            this.getTodos();
          });
      },
      removeTodo() {
        var todoID = document.getElementById('deleteID').value;
        axios.delete('http://localhost:8080/todos/${todoID}').then(() => {
            this.getTodos();
          }).catch((error) => {
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
