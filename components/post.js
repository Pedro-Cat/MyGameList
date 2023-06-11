import styles from "../styles/post.module.css";
import React, { useState } from 'react';


const Post = ({ content, author, defaultIcon }) => {
  const [icon] = useState("https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png");
  const [likes, setLikes] = useState(0);
  const [liked, setLiked] = useState(false);
  

  const handleLike = () => {
    if (!liked) {
      setLikes(likes + 1);
      setLiked(true);
    } else {
      setLikes(likes - 1);
      setLiked(false);
    }
  };

  return (
    <div className={styles.postContainer}>
      <div className={styles.authorIcon} >
        <img src={icon} alt="user icon" />
      </div>
      <h2 className={styles.postAuthor}>{author}</h2>
      <p className={styles.postContent}>{content}</p>
      <form>
        <input
        type="text"
        className={styles.Comment}
        placeholder=" Comment"
        />
      </form>
      <button className={`${styles.LikeBtn} ${liked ? styles.Liked : ''}`} onClick={handleLike}>
        <span className={styles.Heart} role="img" aria-label="heart">❤</span>
      </button>
      <p className={styles.LikeCounter}>{likes}</p>
    </div>
  );
};

export default Post;