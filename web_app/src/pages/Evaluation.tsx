import { useEffect, useState } from 'react';
import { ProgressBar } from "../components/ProgressBar";
import { useNavigate, useOutletContext } from "react-router-dom";
import { ArrowDown } from "../icons/ArrowDown";
import { ArrowUp } from "../icons/ArrowUp";

let intervalId: number;

export const Evaluation = () => {
  const [percentage, setPercentage] = useState(0);
  const [mode, setMode] = useState<'progress' | 'balance' | 'cash'>('progress');

  const navigate = useNavigate();

  const animate = () => {
    intervalId = setInterval(() => {
      setPercentage(prev => {
        const newPercentage = prev + 1;
        return newPercentage > 100 ? 100 : newPercentage;
      });
    }, 50);

  };

  useEffect(() => {
    animate();
  }, []);

  useEffect(() => {
    if (percentage >= 100) {
      clearInterval(intervalId);
      setTimeout(() => setMode('balance'), 500);
    }
  }, [percentage]);

  const setCashMode = () => {
    setMode('cash');
  };


  return (
    <section className="bg-white border-2 border-black rounded-[12px] min-h-[150px] w-full flex flex-col px-2">
      {mode === 'progress' && <ProgressBar percentage={percentage} wait_text="SUBMITTING THE EVALUATION" success_text="Evaluation Submitted!" />}
      {mode === 'balance' && <Balance setCashMode={setCashMode} />}
      {mode === 'cash' && (
        <section className="flex-1 flex flex-col gap-5 py-4">
          <div className="flex gap-2 justify-center items-center">
            <ArrowDown width={20} height={20} className="text-green-500" />
            <p className="text-base font-bold text-black">Bank Withdrawal Process</p>
          </div>

          <p className="text-black font-normal text-xl text-center">Select the bank where you would like to receive your money.</p>

          <div className="flex justify-center gap-4">
            <img src="/paypal.png" alt="paypal" className="h-[80px] w-[90px]" onClick={() =>  navigate('/withdrawal')} />
            <img src="/bank.png" alt="bank" className="h-[80px] w-[130px]" />
          </div>

          <p className="text-center text-neutral-600 font-normal text-sm">If you would like to register a new bank, go to the settings and procced with the registration.</p>
        </section>
      )}
    </section>
  );
};


const Balance = ({ setCashMode }: { setCashMode: () => void; }) => {
  const navigate = useNavigate();
  const [amount] = useOutletContext<[number, (num: number) => void]>();

  return (
    <section className="flex-1 flex flex-col gap-5 py-4">
      <div className="flex gap-2 justify-center items-center">
        <ArrowUp width={20} height={20} className="text-green-500" />
        <p className="text-base font-bold text-black">Your balance has increased!</p>
      </div>

      <div className="flex bg-red-600 rounded-lg h-12 items-center px-6 justify-between">
        <p className="text-white font-normal text-lg">Total Balance:</p>
        <span className="text-white font-bold text-xl">$ {amount}</span>
      </div>

      <div className="flex flex-col gap-0.5 items-center">
        <h5 className="text-2xl font-semibold text-black">CONGRATULATIONS!</h5>
        <p className="text-lg font-normal text-neutral-600">What would you like to do?</p>
      </div>

      <div className="flex flex-col gap-5">
        <button
          className="p-4 bg-red-600 rounded-lg flex justify-center items-center border-2 border-neutral-900"
          onClick={() => navigate('/')}
        >
          <span className="text-white font-medium text-base">Rate new videos</span>
        </button>
        <button
          className="p-4 bg-red-600 rounded-lg flex justify-center items-center border-2 border-neutral-900"
          onClick={setCashMode}
        >
          <span className="text-white font-medium text-base">Withdraw my money</span>
        </button>
      </div>
    </section>
  );
};