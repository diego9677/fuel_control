import { CheckIcon } from "../icons/CheckIcon";
import { CircleNontchIcon } from "../icons/CircleNotchIcon";

export const ProgressBar = ({ percentage, wait_text, success_text }: { percentage: number, wait_text: string, success_text: string }) => {

    return (
      <>
        <div className="flex-1 w-full flex items-center">
          <div className="bg-red-300 h-5 w-full rounded-lg bg-opacity-30 transition-all">
            <div id="progress" className="h-5 bg-red-500 rounded-lg flex justify-center items-center" style={{ width: `${percentage}%` }}>
              <span id="percentage" className="text-white font-bold text-sm">{percentage}%</span>
            </div>
          </div>
        </div>
        <div className="flex items-center gap-1 justify-center">
          {percentage < 100 && (
            <>
              <CircleNontchIcon width={22} height={22} className="animate-spin text-red-600" />
              <p className="text-red-600 font-bold">{wait_text}</p>
            </>
          )}
          {percentage === 100 && (
            <>
              <CheckIcon width={22} height={22} className="text-red-600" />
              <p className="text-red-600 font-bold">{success_text}</p>
            </>
          )}
        </div>
      </>
    );
  };
  