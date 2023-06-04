import styles from "../../styles/settings.module.css" 
import React, { useState } from 'react';
import Link from "next/link";
import CardPopUp from "../../components/cardpopup"
import Layout from "../../components/Layout";

const ProfileSettings= () => { 

  const [activeTab, setActiveTab] = useState('profile');

  const handleTabChange = (tab) => {
    setActiveTab(tab);
  };
  
  const cardData = [
    { id: 1, title: 'Game 1' },
    { id: 2, title: 'Game 2' },
    { id: 3, title: 'Game 3' },
    { id: 4, title: 'Game 4' },
    { id: 5, title: 'Game 5' },
  ];

    return (
      <>
        <Link href="/profilepage">
        <img className={styles.back} src="https://cdn.discordapp.com/attachments/443897310930534422/1111823092357005312/back_button.png" alt="back"/>
        </Link>
        <h1 className={styles.configuracao}>SETTINGS</h1>
        <div>
      <nav className={styles.navbar}>
        <ul className={styles.navbar}>
          <li
            className={activeTab === 'profile' ? 'active' : ''}
            onClick={() => handleTabChange('profile')}
          >
            <Link href="/settings#profile">PROFILE</Link>
          </li>
          <li
            className={activeTab === 'security' ? 'active' : ''}
            onClick={() => handleTabChange('security')}
          >
            <Link href="/settings#security">SECURITY</Link>
          </li>
        </ul>
      </nav>

      <hr className={styles.line} />
    
      {activeTab === 'profile' && (
        <div id="profile">
          <form>
          <label className={styles.settingsUsername}>
            USERNAME:
            <br/>
            <input
              type="text"
              className={styles.usernameinputField}
            />
            <br/>
          </label>
          <label className={styles.settingsDescription}>
            DESCRIPTION:
            <br/>
            <textarea
              className={styles.descriptioninputField}
            ></textarea>
            <br/>
          </label>
          <label className={styles.settingsIcon}>
            PROFILE ICON:
            <br/>
            <br/>
            <input
              type="file"
              accept="image/*"
            />
            <br/>
          </label>
          <label className={styles.settingsProfileBackground}>
            PROFILE BACKGROUND:
            <br/>
            <br/>
            <input
              type="file"
              accept="image/*"           
            />
          </label>
          <br/>
          <button className={styles.save} type="submit">SAVE</button>
        </form>
        <>
        <h1 className={styles.title2}>CHANGE TOP 5</h1>
        <div className={styles.changetop5}>
      {cardData.map((card) => (
        <CardPopUp key={card.id} title={card.title} />
      ))}
      </div>
      <button className={styles.change} type="submit">CHANGE</button>
      </>
        </div>
      )}

      {activeTab === 'security' && (
        <div id="security">
          <div>
        <Link href="/profilepage">
        <img className={styles.back} src='https://cdn.discordapp.com/attachments/443897310930534422/1111823092357005312/back_button.png' alt="voltar"/>
        </Link>
        <form>
        <label className={styles.email}>
            EMAIL:
            <br/>
            <input
              type="text"
              className={styles.emailinputField}
            />
            <br/>
          </label>
          <label className={styles.password}>
            PASSWORD:
            <br/>
            <input
              type="text"
              className={styles.passwordinputField}
            />
            <br/>
          </label>
        </form>
        <button className={styles.change2} type="submit">CHANGE</button>
        <button className={styles.change3} type="submit">CHANGE</button>
        </div>
        </div>
      )}
    </div>

        
    </>
    );
};
  
export default ProfileSettings;