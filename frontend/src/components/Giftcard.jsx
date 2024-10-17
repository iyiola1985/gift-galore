// src/GiftCard.js
import React from 'react';

const GiftCard = ({ image, name, description, price }) => {
  return (
    <div className="gift-card">
      <img src={image} alt={name} />
      <h2>{name}</h2>
      <p>{description}</p>
      <p>Price: ${price}</p>
    </div>
  );
};

export default GiftCard;
