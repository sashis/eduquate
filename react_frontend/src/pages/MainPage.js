import {PageHeader, PageMain} from './PageLayout';

const MainPage = () => {
  return (
      <main>
        <PageHeader
            title='Образовательный портал'
            lead={`С нами вы приобретете самые актуальные знания 
                    и станете востребованным специалистом`}
        >
        </PageHeader>
        <PageMain>
          Главная страница
        </PageMain>
      </main>
  );
};

export default MainPage;