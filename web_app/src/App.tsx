import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Root } from "./pages/Root";
import { Home } from "./pages/Home";
import { Evaluation } from "./pages/Evaluation";
import { Withdrawal } from "./pages/Withdrawal";

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    children: [
      {
        path: '',
        element: <Home />
      },
      {
        path: '/evaluation',
        element: <Evaluation />
      },
      {
        path: '/withdrawal',
        element: <Withdrawal />
      }
    ]
  }
]);

function App() {
  return <RouterProvider router={router} />
}

export default App
