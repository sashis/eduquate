import {Container} from 'react-bootstrap';

const Footer = () => (
    <footer className='mt-5'>
      <Container className='text-center'>
        <hr/>
        <p>&copy; EDUQUATE {new Date().getFullYear()}</p>
      </Container>
    </footer>
);

export default Footer;