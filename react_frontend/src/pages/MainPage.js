import {useEffect, useState} from 'react';
import {PageHeader, PageMain} from './PageLayout';
import {CourseList} from '../components/CourseList';
import Api from '../services/api';

const getTopCourses = (courses, top_count = 3) => {
  const topCourses = [...courses];
  topCourses.sort((a, b) => -(a?.num_students - b?.num_students));
  return topCourses.slice(0, top_count);
};

const MainPage = () => {
  const [courses, setCourses] = useState([]);
  useEffect(() => {
    Api.getCourses().then(newCourses => {
      const topCourses = getTopCourses(newCourses, 3);
      setCourses(topCourses);
    });
  }, []);

  return (
      <main>
        <PageHeader
            title='Образовательный портал'
            lead={`С нами вы приобретете самые актуальные знания 
                    и станете востребованным специалистом`}
        >
        </PageHeader>
        <PageMain>
          <h2 className='mb-5'>Популярные курсы</h2>
          <CourseList courses={courses}/>
        </PageMain>
      </main>
  );
};

export default MainPage;