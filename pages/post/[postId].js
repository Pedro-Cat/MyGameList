import { useRouter } from 'next/router';
import Post from "../components/post"

const PostPage = () => {
  const router = useRouter();

  return (
    <div>
      <h1>Post Page</h1>
    </div>
  );
};

export default PostPage;
