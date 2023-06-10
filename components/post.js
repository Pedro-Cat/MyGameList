import styles from "../styles/post.module.css";
import React, { useState } from 'react';


const Post = ({ content, author, defaultIcon }) => {
  const [icon] = useState("https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png");

  return (
    <div className={styles.postContainer}>
      <div className={styles.authorIcon} >
        <img src={icon} alt="user icon" />
      </div>
      <h2 className={styles.postAuthor}>{author}</h2>
      <p className={styles.postTitle}>{content}</p>
    </div>
  );
};

export default Post;

