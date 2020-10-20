import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';
import { Content } from './Content';
// or

function handleSubmit(response) {
    // TODO replace with name from oauth
    // console.log(response.nt.Ad);
    // let name = response.nt.Ad;
    // Socket.emit('new google user', {
    //     'name': name,
    // });
    
    // console.log('Sent the name ' + name + ' to server!');
    
    console.log(response);
    // console.log(response.profileObj.imageUrl);
    let name = response.nt.Ad;
    let imageURL = response.profileObj.imageUrl;
    
    ReactDOM.render(<Content />, document.getElementById('content'));
    console.log("woohoo");
    Socket.emit('new google user', {
        'name': name, 'imageURL':imageURL
    });
    
}

export function GoogleButton() {
    
    return <GoogleLogin
    clientId="938469198889-n1k7dgf0oagn6qclrv173j31g5joh6rr.apps.googleusercontent.com"
    onSuccess={handleSubmit}
    onFailure={handleSubmit}
    cookiePolicy={'single_host_origin'}/>
}