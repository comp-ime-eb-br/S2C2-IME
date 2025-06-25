import React from "react";

interface CardProps {
  children: React.ReactNode;
  bgColor?: string;
}

const Card: React.FC<CardProps> = ({ children, bgColor = "bg-gray-800" }) => {
  return (
    <div className={`p-4 rounded-2xl shadow-md ${bgColor}`}>
      {children}
    </div>
  );
};

export default Card;