import * as React from 'react';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';
import { Socket } from './Socket';
import { Content } from './Content';

function handleSubmit(response) {
  const { name } = response.profileObj;
  const imageURL = response.profileObj.imageUrl;

  Socket.emit('new google user', {
    name, imageURL,
  });

  ReactDOM.render(<Content />, document.getElementById('content'));
  console.log('woohoo');
}

export function GoogleButton() {
  return (
    <GoogleLogin
      clientId="938469198889-n1k7dgf0oagn6qclrv173j31g5joh6rr.apps.googleusercontent.com"
      onSuccess={handleSubmit}
      onFailure={handleSubmit}
      cookiePolicy="single_host_origin"
    />
  );
}
