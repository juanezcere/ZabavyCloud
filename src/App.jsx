import { TopBar } from './components/TopBar';

import { FootBar } from './components/FootBar';

function App() {
  return (
    <main className='text-foreground bg-background'>
      <TopBar />
      <section className='mx-auto xl:flex xl:flex-cols-2 xl:justify-center xl:items-center'>
        <article className='p-5'>
            <h1>Welcome</h1>
        </article>
        <article className='p-5'>
            <h1>Welcome 2</h1>
        </article>
      </section>
      <FootBar />
    </main>
  );
}

export default App;
