import React from 'react';
import './HomePage.css'; // Optional for styling
import SearchItem from './SearchItem';

const HomePage = () => {
  return (
    <div className="landing-page">
      <header className="hero">
        
        <h2>Affordable gift a touch of a button suitable gifts for various events
A free, private, gift registry trusted by over two million members. You can get gifts right. Every time.™️ Set it up once, use it for a lifetime.</h2>
    
      <button className="cta-button">Start shopping</button>
      </header>
      <div className="image-container">
            <img src="https://musicarts.wpenginepowered.com/wp-content/uploads/2018/11/kira-auf-der-heide-475623-unsplash-scaled.jpg" alt="Describtion" width="100%"height="auto"/>
            <div class="overlay-text">"Discover the Perfect Gift for Every Occasion! 🎁✨ From heartfelt treasures to unique finds, create unforgettable moments for your loved ones today!"</div>
            
              </div>

      <section className="features">
        <h2>🌟 Welcome to Gift Galore! 🌟
At Gift Galore, we believe every gift tells a story. Whether you're celebrating a birthday, anniversary, or just want to show someone you care, we have the perfect treasures to make those moments unforgettable.
Explore our curated selection of heartfelt gifts, unique finds, and personalized treasures designed to delight your loved ones. Each item is handpicked with love, ensuring you can find something special for everyone on your list.
Dive into a world of thoughtful surprises and let your gifting journey begin! Because the best gifts are the ones that come from the heart. </h2>
        <div className="feature">

        </div>
      </section>

      <footer className="footer">
        <p>&copy; {new Date().getFullYear()} Your Company Name. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;
