    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';


export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    const [urls, seturls] = React.useState([]);
    var index = 0;
    var mString = '';
    const [users, setUser] = React.useState([]);
    // var messageBody = document.querySelector('#messageBody');
    // messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
    
    const [imageURL, setURL]=React.useState([]);
    
    const[mURL, setmURL]=React.useState([])
    const[dbUser, setdbUser]=React.useState([])
    
    const[isURL, setisURL]=React.useState([])
    
    function getNewAddresses() {
        
        
        
        React.useEffect(() => 
        {
            Socket.on('addresses received', (data) => {
                

                setAddresses(data['allAddresses']);

                setUser(data['numUsers']);
                setdbUser(data['User']);
                
                setURL(data['imageURL']);
                
                setisURL(data['isUrl']);
                
                setmURL(data['address']);
                
                seturls(data['checkUrl']);
              
                // <img src = {address.substring(0,9)=="wall-Ebot" ? '' : {{imageURL}} } />
                // {% if address.substring(0,9) == "wall-Ebot" %}
                //     <img src = "">
                //     {% else %}
                //     <img src = {imageURL}>
                //     {% endif %}
             
                
            })
        });
    }
    
    function PutMessage(props)
    {
        console.log("values: " + index + urls[index]);
        
        var res = props.address.substr(props.address.length-4);
        console.log(res);
        
        
        if (urls[index] != "1"){
            
            index++;
            if( res==".png" || res==".jpg" || res==".gif" )
            {
                
                return ( <div style={{display: "inline-block"}}>
                <img src = { props.address.substring(0,9)=="wall-Ebot" ? "https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif" : imageURL[index-1] } width="30" height="30" />
                <p>{dbUser[index-1]}: </p><a href={urls[index-1]}>{props.address}   </a>
                <img src={urls[index-1]} width="100" height="100"/>
                </div> )

            }
            else{
           
            return ( <div style={{display: "inline-block"}}>
            <img src = { props.address.substring(0,9)=="wall-Ebot" ? "https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif" : imageURL[index-1] } width="30" height="30" />
            <p>{dbUser[index-1]}: </p><a href={urls[index-1]}>{props.address}</a> </div> )
            }
            
        }
        else{
            
            index++;
            return( <div>
            <img src = { props.address.substring(0,9)=="wall-Ebot" ? "https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif" : imageURL[index-1] } width="30" height="30" />
                <p style = {{display: "inline"}} >{props.address}</p>
                </div> )
        }
        
        
        
    }

    
    getNewAddresses();
    
    var chatarea = {
        backgroundColor: "lightblue",
        minWidth: "150px",
        outlineStyle: "solid",
        outlineWidth: "3px",
        height: "770px",
        width: "970px",
        overflow:"auto",
        display:"flex",
    };

    return (
        <div>
            <h1 style={{fontFamily:"verdana", backgroundColor: "lightblue", textAlign: "center"}}>WALL-E Chat Room! ({ users } member online)</h1>
            <div style={chatarea}>
                <ul>
                    {
                    addresses.map((address, index) => <li style= {{fontWeight: address.substring(0,9)=="wall-Ebot" ? 'bold' : 'none'}}>
                    <PutMessage address={address}/>
                    </li>)
                    }
                </ul>
            </div>
            <Button />
            
            <img class="center" src="https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif"/>
        </div>
        
    );
}
