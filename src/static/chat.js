var socket = io();

function addMessage(data, currentUser) {
  var { user, content, sended_at } = data;

  var chat = document.querySelector('#chat');

  var item = document.createElement('li');

  var author = document.createElement('span');
  author.innerHTML = user === currentUser ? 'você' : user;
  author.classList.add('text-muted');
  item.appendChild(author);

  var bodyMessage = document.createElement('p');
  bodyMessage.innerHTML = content;
  bodyMessage.classList.add('my-2');
  item.appendChild(bodyMessage);

  var date = document.createElement('span');
  date.innerHTML = sended_at;
  date.classList.add('text-muted');
  item.appendChild(date);

  chat.appendChild(item);
}

socket.on('connect', function() {
  var currentUser = document.querySelector('#nickname').value;

  socket.on('recieve_message', function(data) {
    addMessage(data, currentUser);
  });

  document.querySelector('#chat-form')
    .addEventListener('submit', function(e) {
      e.preventDefault();

      var msg = document.querySelector('#msg');

      if (msg === '') {
        return;
      }

      socket.emit('send_message', { msg: msg.value });

      msg.value = '';
    });
});
