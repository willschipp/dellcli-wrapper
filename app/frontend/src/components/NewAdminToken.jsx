import React, { useState } from 'react';
import { Form, TextArea, Button, Well, View, TextField, Content, Heading  } from '@adobe/react-spectrum';

function NewAdminToken() {

    const [token, setToken] = useState({})
    const [tokenName, setTokenName] = useState("");
    const [signingSecret, setSigningSecret] = useState("");
    const [tokenExpiration, setTokenExpiration] = useState("");
    const [refreshExpiration, setRefreshExpiration] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        try {
            const response = await fetch('/admin/token',{
                method:'POST',
                headers: {
                    'Content-type':'application/json'
                },
                body: JSON.stringify({
                    "token-name": tokenName,
                    "jwt-signing-secret": signingSecret,
                    "access-token-expiration": tokenExpiration,
                    "refresh-token-expiration": refreshExpiration
                })
            });
            if (!response.ok) {
                throw new Error(`http error! status: ${response.status}`);
            }
            const result = await response.json();
            setToken(result)
        } catch (error) {
            console.error(error);
        }
    }

    return (
        <Content width="calc(80% - size-1000)">
            <Heading level={4}>Generate an Admin Token</Heading>
            <p>
                (just make up some stuff here...)
            </p>
            <Form onSubmit={handleSubmit}>
                <TextField label="Token Name" value={tokenName} onChange={setTokenName}/>
                <TextArea label="Copy & Paste your build file here" isRequired={true} value={signingSecret} onChange={setSigningSecret} height="size-3000"/>
                <TextField label="Token Expiration Time" value={tokenExpiration} onChange={setTokenExpiration}/>
                <TextField label="Refresh Token Expiration" value={refreshExpiration} onChange={setRefreshExpiration}/>
                <Button type="submit" maxWidth="size-1000">Submit</Button>
            </Form>
            <View>
                <Well marginTop="size-100">
                    <pre style={{
                        whiteSpace:'pre-wrap',
                        margin: 0,
                        fontFamily: 'monospace',
                        maxHeight: '500px',
                        overflow: 'auto',
                        width:'80%'
                    }}>
                        {token.length <= 0 ? "" : JSON.stringify(token,null,2)}
                    </pre>                    
                </Well>
            </View>
        </Content>
    )
}

export default NewAdminToken;

