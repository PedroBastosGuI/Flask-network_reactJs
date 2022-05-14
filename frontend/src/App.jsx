import {CameraInit} from './Components/Camera';
import { Header } from './Components/header';
import {Global} from './styles/global';
import {Table} from './Components/table';
function App() {
  return (
    <>
      <Global/>
      <Header/>
      <CameraInit/>
      <Table/>
    </>
  );
}

export default App;