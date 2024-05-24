export const ArrowUp = ({ width, height, color, className }: { width: number, height: number; color?: string; className?: string; }) => {
    return (
        <svg xmlns="http://www.w3.org/2000/svg" width={width} height={height} className={className} color={color} viewBox="0 0 16 16">
            <path fill="currentColor" fillRule="evenodd" d="M8 14.75a.75.75 0 0 1-.75-.75V3.81L4.53 6.53a.75.75 0 0 1-1.06-1.06l4-4a.75.75 0 0 1 1.06 0l4 4a.75.75 0 0 1-1.06 1.06L8.75 3.81V14a.75.75 0 0 1-.75.75" clipRule="evenodd" />
        </svg>
    );
};
