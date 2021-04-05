import React from 'react';
import {Nav, Navbar} from 'react-bootstrap';

const AppBar = () => {
  return (
      <Navbar variant='dark' bg='dark' expand='md' sticky='top'>
        <Navbar.Brand href="#">
          <span className='text-white-50'>EDU</span>QUATE
        </Navbar.Brand>
        <Navbar.Toggle aria-controls='basic-navbar-nav'/>
        <Navbar.Collapse id='basic-navbar-nav' className='justify-content-end'>
          <Nav as="ul">
            <Nav.Link className='mx-2'>Контакты</Nav.Link>
            <Nav.Link className='mx-2'>Курсы</Nav.Link>
            <Nav.Link className='mx-2'>Вход</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
  );
};

export default AppBar;