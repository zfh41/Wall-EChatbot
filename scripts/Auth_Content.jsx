    
import * as React from 'react';

import { GoogleButton } from './GoogleButton';
import { Socket } from './Socket';

export function Auth_Content() {
    const [accounts, setAccounts] = React.useState([]);
    
    function getAllAccounts() {
        React.useEffect(() => {
            Socket.on('users updated', (data) => {
                let allAccounts = data['allUsers'];
                console.log("Received accounts from server: " + allAccounts);
                setAccounts(allAccounts);
            })
        });
    }
    
    
    
    getAllAccounts();
    
    // TODO use these accounts for something
    
    return (
        <div>
            <h1>Log in with OAuth!</h1>
            <GoogleButton />
        </div>
        
    );
}
