import { useEffect, useState } from "react";
import { ProgressBar } from "../components/ProgressBar";
import { CheckIcon } from "../icons/CheckIcon";
import { useNavigate, useOutletContext } from "react-router-dom";

let intervalId: number;

export const Withdrawal = () => {
    const [percentage, setPercentage] = useState(0);
    const [mode, setMode] = useState<'progress' | 'balance' | 'cash'>('progress');

    const navigate = useNavigate();
    const [amount, setAmount] = useOutletContext<[number, (num: number) => void]>();

    const animate = () => {
        intervalId = setInterval(() => {
            setPercentage(prev => {
                const newPercentage = prev + 1;
                return newPercentage > 100 ? 100 : newPercentage;
            });
        }, 50);

    };

    const showBrowserNotification = () => {
        // Crear y mostrar la notificación del navegador
        new Notification('PayPal', {
            body: `You have received a transfer of $${amount}`,
            icon: 'paypalmini.png',
            // image: 'minilogo.png',
        });

        setAmount(0);
    };

    useEffect(() => {
        animate();
    }, []);

    useEffect(() => {
        if (percentage >= 100) {
            clearInterval(intervalId);
            showBrowserNotification();
            setTimeout(() => setMode('balance'), 1000);
        }
    }, [percentage]);

    return (
        <section className="bg-white border-2 border-black rounded-[12px] min-h-[150px] w-full flex flex-col px-2">
            {mode === 'progress' && <ProgressBar percentage={percentage} wait_text="Withdrawal in progress" success_text="Withdrawal completed!" />}
            {mode === 'balance' && (
                <section className="flex-1 flex flex-col gap-5 py-4">
                    <div className="flex gap-2 justify-center items-center">
                        <CheckIcon width={20} height={20} className="text-green-500" />
                        <p className="text-base font-bold text-black">Withdrawal completed!</p>
                    </div>

                    <div className="flex bg-red-600 rounded-lg h-12 items-center px-6 justify-between">
                        <p className="text-white font-normal text-lg">Total Balance:</p>
                        <span className="text-white font-bold text-xl">$ {amount}</span>
                    </div>

                    <div className="flex flex-col gap-0.5 items-center pb-5 border-b border-neutral-300">
                        <h5 className="text-2xl font-semibold text-black">Withdrawal Successfull!</h5>
                        <p className="text-lg font-normal text-neutral-600 text-center">Within 60 minutes, the withdrawal amount will be in your bank account, thank you!</p>
                    </div>

                    <p className="text-xl font-bold text-black text-center">Rate more videos and continue to earn commissions!</p>

                    <div className="flex flex-col gap-5">
                        <button
                            className="p-4 bg-red-600 rounded-lg flex justify-center items-center border-2 border-neutral-900"
                            onClick={() => navigate('/')}
                        >
                            <span className="text-white font-medium text-base">RATE MORE ADS</span>
                        </button>
                    </div>
                </section>
            )}
        </section>
    );
};
