import { useEffect, useState } from "react";
import { Outlet } from 'react-router-dom';

export const Root = () => {
  const [amount, setAmount] = useState(7819.44);

  useEffect(() => {
    if ('Notification' in window) {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          console.log('Permiso para mostrar notificaciones concedido');
        }
      });
    }
  }, []);

  return (
    <main className="fixed w-full z-10" style={{ height: window.innerHeight }}>
      <div className="w-full md:w-[430px] mx-auto h-full overflow-auto bg-image">
        <section className="bg-black bg-opacity-15 h-full overflow-auto py-5 px-2 flex flex-col gap-5 w-full">
          <header className="h-16 bg-white flex rounded-lg border border-neutral-300 items-center justify-between">
            <img src="/minilogo.png" alt="logo" className="h-[50px] w-[62px]" />

            <div className="bg-red-600 w-32 h-10 rounded-lg mr-4 flex justify-center items-center">
              <span className="text-white font-bold text-lg">$ {amount}</span>
            </div>
          </header>

          <Outlet context={[amount, setAmount]} />
        </section>
      </div>
    </main>
  );
};
