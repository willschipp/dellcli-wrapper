import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Grid, View , defaultTheme, Provider, Content } from '@adobe/react-spectrum';

import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';

import Home from './components/Home';
import Menu from './components/Menu';
import NewAdminToken from './components/NewAdminToken';

function App() {

  return (
    <Provider theme={defaultTheme}>
      <Router>
      <Grid 
          areas={['header header', 'sidebar content','footer footer']} 
          columns={['1fr','3fr']} 
          rows={['size-1000','auto','size-1000']} 
          height="100vh" 
          gap="size-100"
          justifyContent="center">
          <View gridArea="header">
            <AppHeader/>
          </View>
          <View gridArea="sidebar">
            <Menu/>
          </View>
          <View gridArea="content">   
            <Content>      

                <Routes>
                  <Route exact path="/" element={<Home/>}/>
                  <Route path="/admin_token" element={<NewAdminToken/>}/>
                </Routes>          
              
            </Content>
          </View>
          <View gridArea="footer">
            <AppFooter/>
          </View>
        </Grid>        
      </Router>
    </Provider>
  )
}

export default App
