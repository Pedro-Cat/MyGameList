import Post from "../components/post"
import styles from "../styles/feed.module.css"
import React, { useState } from 'react';
import Link from "next/link";


const posts = [
  { id: 1, content: 'ipsum dolor sit amet, consectetur adipiscing elit. Aenean sagittis blandit ligula, in pellentesque arcu lacinia a. Suspendisse eu tellus nec arcu blandit vulputate vitae non lacusLorem.', author: 'Autor 1' },
  { id: 2, content: 'ipsum dolor sit amet, consectetur adipiscing elit. Aenean sagittis blandit ligula, in pellentesque arcu lacinia a. Suspendisse eu tellus nec arcu blandit vulputate vitae non lacusLorem.', author: 'Autor 2' },
  { id: 3, content: 'ipsum dolor sit amet, consectetur adipiscing elit. Aenean sagittis blandit ligula, in pellentesque arcu lacinia a. Suspendisse eu tellus nec arcu blandit vulputate vitae non lacusLorem.', author: 'Autor 3' },
];

const Feed = () => {

  const [icon] = useState("https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png");

  return (
    <div className={styles.Container}>
        <Link href="/">
        <img className={styles.back} src="https://cdn.discordapp.com/attachments/443897310930534422/1111823092357005312/back_button.png" alt="back"/>
        </Link>
        <h1 className={styles.feed}>FEED</h1>
        <hr className={styles.line} />
        <div>
          <img className={styles.icon} src={icon} alt="Icon"/>
          <form className={styles.postFormContainer}>
            <textarea
            className={styles.UserPost}
            type="text"
            placeholder="what's happening?"
            maxLength={320}
            />
            <button className={styles.sendButton} type="submit"/>
          </form>
        </div>
        <div className={styles.feedContainer}>
        {posts.map((post) => (
            <Post key={post.id} content={post.content} author={post.author} />
        ))}
        </div>
    </div>
  );
};

export default Feed;
