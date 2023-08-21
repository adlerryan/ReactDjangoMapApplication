import React, { useState, useEffect } from 'react';
import { slide as Menu } from 'react-burger-menu';
import { FaBars, FaSearch } from 'react-icons/fa';

function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isSearchOpen, setIsSearchOpen] = useState(false);
  const [menuWidth, setMenuWidth] = useState('50%');

  useEffect(() => {
    if (window.innerWidth <= 768) {
      setMenuWidth('80%');
    } else {
      setMenuWidth('50%');
    }
  }, []);

  const handleMenuToggle = () => {
    setIsMenuOpen(!isMenuOpen);
    setIsSearchOpen(false);
  };

  const handleSearchToggle = () => {
    setIsSearchOpen(!isSearchOpen);
    setIsMenuOpen(false);
  };

  const headerStyle = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: window.innerWidth <= 768 ? '0.5em' : '1em',
    backgroundColor: '#000',
    color: '#FFD700',
    position: 'absolute',
    zIndex: 9999,
    width: '100%',
    maxHeight: '60px',
    overflow: 'hidden'
  };

  const menuStyles = {
    bmMenu: {
      top: 'unset',
      bottom: 'auto',
      borderRadius: '0 0 10px 10px',
      padding: '1em',
      backgroundColor: '#800080',
      transition: 'width 0.3s ease',
    },
    bmBurgerButton: { display: 'none' },
    bmMenuWrap: { 
      position: 'absolute', 
      top: window.innerWidth <= 768 ? '40px' : '60px', 
      right: 0, 
      width: menuWidth, 
      height: 'auto' 
    },
  };

  return (
    <header style={headerStyle}>
      <div style={{ display: 'flex', alignItems: 'center' }}>
        <div style={{ zIndex: 101, marginRight: '1em', maxWidth: '70%' }}>
          {isSearchOpen ? <input type="text" placeholder="Search..." style={{ width: '100%' }} /> : <FaSearch size={24} onClick={handleSearchToggle} style={{ cursor: 'pointer' }} />}
        </div>
      </div>
      <div style={{ position: 'relative' }}>
        <FaBars size={24} onClick={handleMenuToggle} style={{ cursor: 'pointer' }} />
        <Menu
          right
          width={menuWidth}
          isOpen={isMenuOpen}
          customBurgerIcon={false}
          styles={menuStyles}
        >
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <a id="home" className="menu-item" href="/">
              Home
            </a>
            <a id="about" className="menu-item" href="/about">
              About
            </a>
            <a id="contact" className="menu-item" href="/contact">
              Contact
            </a>
            <a id="settings" className="menu-item" href="/settings">
              Settings
            </a>
          </div>
        </Menu>
      </div>
    </header>
  );
}

export default Header;
