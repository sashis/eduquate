import {Card, CardDeck, Col} from 'react-bootstrap';
import {choosePlural} from '../services/utils';

export const CourseList = ({courses}) => {
  const courseList = courses.map(course => {
    const {url, name, tutor, num_lessons} = course;
    return <CourseCard key={url} title={name} tutor={tutor.full_name}
                       numLessons={num_lessons}/>;
  });
  return (
      <CardDeck>
        {courseList.length === 0 ?
            <div>Нет информации о курсах</div> :
            courseList}
      </CardDeck>
  );
};

export const CourseCard = props => {
  const {title, tutor, numLessons} = props;
  const pluralLessons = choosePlural(numLessons,
      ['занятие', 'занятия', 'занятий']);

  return (
      <Col md={6} lg={4} className='mb-4 align-items-stretch'>
        <Card bg='light' className='mx-0 h-100'>
          <Card.Body>
            <Card.Title>{title}</Card.Title>
          </Card.Body>
          <Card.Footer>
            <small className='text-muted d-flex justify-content-between'>
              <span>{tutor}</span>
              <span>{`${numLessons} ${pluralLessons}`}</span>
            </small>
          </Card.Footer>
        </Card>
      </Col>
  );
};
