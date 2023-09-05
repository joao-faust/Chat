function validatePassword(){
  const password1 = document.querySelector('#password-1');
  const password2 = document.querySelector('#password-2');

  if (password1.value !== password2.value) {
    password2.setCustomValidity('Senhas não conferem!');
  } else {
    password2.setCustomValidity('');
  }
}
