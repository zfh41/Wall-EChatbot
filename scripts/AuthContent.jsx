import * as React from 'react';

import { GoogleButton } from './GoogleButton';
import { Socket } from './Socket';

export function AuthContent() {
  const [accounts, setAccounts] = React.useState([]);

  function getAllAccounts() {
    React.useEffect(() => {
      Socket.on('users updated', (data) => {
        const allAccounts = data.allUsers;
        console.log(`Received accounts from server: ${allAccounts}`);
        setAccounts(allAccounts);
      });
    });
  }

  getAllAccounts();

  // TODO use these accounts for something

  return (
    <div>
      <h1 style={{ fontFamily: 'verdana' }}>Join Wall-E Chatroom!</h1>
      <GoogleButton />
      {' '}
      <br />
      {' '}
      <br />

      <img alt="Wall-EBot!!!" src="https://66.media.tumblr.com/420ad6eedfdbac0d8d047743a6462b85/tumblr_o1489hnyJJ1rey868o1_500.gif" />

    </div>

  );
}
