import Link from "next/link";
import Settings from "../settings";
import styles from "../../styles/profilepage.module.css"
import Card from "../../components/card" 
import React, { Fragment, useState } from 'react';
import { useRouter } from 'next/router';
import Layout from "../../components/Layout";

const ProfilePage= () =>  {
  const router = useRouter();

  const profileId = router.query.ProfileId;
  
  const defaultProfilePicture = 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png';
  const defaultBackgroundPicture = 'https://www.unfe.org/wp-content/uploads/2019/04/SM-placeholder.png';
  const [username] = useState('USERNAME');
  const [description] = useState('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sagittis blandit ligula, in pellentesque arcu lacinia a. Suspendisse eu tellus nec arcu blandit vulputate vitae non lacus.');
  const [profilePicture] = useState(defaultProfilePicture);
  const [backgroundPicture] = useState(defaultBackgroundPicture);

  const cardData = [
    { id: 1, title: 'Game 1' },
    { id: 2, title: 'Game 2' },
    { id: 3, title: 'Game 3' },
    { id: 4, title: 'Game 4' },
    { id: 5, title: 'Game 5' },
  ];

    return (
        <div className={styles.profileContainer}>
          <div className={styles.fundo}></div>
          <img className={styles.profilebackground} src= {backgroundPicture} alt="Foto de fundo do perfil" />
          <img className={styles.profileicon} src= {profilePicture} alt="Foto de perfil" />
          <h1 className={styles.username}>{username}</h1>
          <p className={styles.userdescription}>{description}</p>
          <>
          <Link href="/settings">
          <img className={styles.settings} src='https://cdn-icons-png.flaticon.com/512/1159/1159633.png' alt="voltar"/>
          </Link>
          </>
          <Fragment>
          <h1 className={styles.title2}>TOP 5 GAMES</h1>
        <div className={styles.top5games}>
          {cardData.map((card) => (
            <Card key={card.id} title={card.title} />
          ))}
        </div>
          </Fragment>
        </div>
    );
}

export default ProfilePage;