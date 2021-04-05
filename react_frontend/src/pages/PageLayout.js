import {Container, Jumbotron} from 'react-bootstrap';

export const PageHeader = ({title, lead, children}) => {
  return (
      <Jumbotron className='py-5'>
        <Container>
          <h1 className='display-4'>{title}</h1>
          {lead && <p className='lead'>{lead}</p>}
          {children}
        </Container>
      </Jumbotron>
  );
};

export const PageMain = ({children}) => (
    <Container>{children}</Container>
);
