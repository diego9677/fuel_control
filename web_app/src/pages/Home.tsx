import { useRef, useState } from 'react';
import { StarIcon } from "../icons/StarIcon";
import { useNavigate, useOutletContext } from "react-router-dom";

export const Home = () => {
    const [isPlaying, setIsPlaying] = useState(false);
    const [starts, setStarts] = useState<{ [num: string]: number; }>({ '1': 0, '2': 0, '3': 0, '4': 0, '5': 0 });

    const videoRef = useRef<HTMLVideoElement>(null);
    const [amount, setAmount] = useOutletContext<[number, (num: number) => void]>();

    const navigate = useNavigate();


    const showBrowserNotification = () => {
        // Crear y mostrar la notificación del navegador
        new Notification('ProfiTok', {
            body: 'You received $14.24 for watching and rating a video!',
            icon: 'minilogo.png',
            // image: 'minilogo.png',
        });
    };

    const clickPlay = () => {
        if (isPlaying) {
            videoRef.current?.pause();
            setIsPlaying(false);
        } else {
            videoRef.current?.play();
            setIsPlaying(true);
        }
    };

    const clickScore = (num: string) => {
        const cont = Number(num);
        for (let i = 1; i <= Object.keys(starts).length; i++) {
            if (i <= cont) {
                setStarts(prev => ({ ...prev, [i]: 1 }));
            } else {
                setStarts(prev => ({ ...prev, [i]: 0 }));
            }
        }

        setTimeout(() => {
            setAmount(Number((amount + 14.24).toFixed(2)));
            navigate('/evaluation');
            showBrowserNotification();
        }, 1000);
    };

    return (
        <>
            <main className="h-[700px] w-full relative flex justify-center items-center" onClick={clickPlay}>
                <video ref={videoRef} src="/video1.mp4" className="object-cover h-full w-full rounded-lg"></video>

                {!isPlaying && (
                    <div className="absolute w-20 h-24 flex justify-center items-center">
                        <img src="play.png" alt="play" className="w-full h-full" />
                    </div>
                )}
            </main>

            <section className="bg-white pr-2 rounded-lg border border-slate-300 flex justify-between items-center py-2">
                <div className="flex gap-1 items-center">
                    <img src="/minilogo.png" alt="logo" className="h-[40px] w-[55px]" />

                    <div className="flex flex-col">
                        <p className="text-lg font-bold text-neutral-800">lifeisbeautiful4044</p>
                        <p className="text-sm font-normal text-neutral-600">💫Life is beautiful💫</p>
                    </div>
                </div>
                <div className="bg-green-600 bg-opacity-40 h-8 w-24 rounded-lg flex justify-center items-center">
                    <span className="text-green-800 font-bold text-base">+ $14.24</span>
                </div>
            </section>

            <section className="flex flex-col gap-5 p-4 items-center bg-white rounded-lg">
                <p className="text-lg font-semibold text-neutral-800">How do you rate the above video? Please give a score from 1 to 5.</p>

                <div className="flex gap-4 items-center">
                    <span className={starts['1'] === 1 ? 'text-yellow-500' : 'text-neutral-500'} onClick={() => clickScore('1')}>
                        <StarIcon width={40} height={40} />
                    </span>
                    <span className={starts['2'] === 1 ? 'text-yellow-500' : 'text-neutral-500'} onClick={() => clickScore('2')}>
                        <StarIcon width={40} height={40} />
                    </span>
                    <span className={starts['3'] === 1 ? 'text-yellow-500' : 'text-neutral-500'} onClick={() => clickScore('3')}>
                        <StarIcon width={40} height={40} />
                    </span>
                    <span className={starts['4'] === 1 ? 'text-yellow-500' : 'text-neutral-500'} onClick={() => clickScore('4')}>
                        <StarIcon width={40} height={40} />
                    </span>
                    <span className={starts['5'] === 1 ? 'text-yellow-500' : 'text-neutral-500'} onClick={() => clickScore('5')}>
                        <StarIcon width={40} height={40} />
                    </span>
                </div>
            </section>
        </>
    );
};
