import { useState } from "react";
import "./Image.css";
import axios from "axios";

const Image = () => {
    const [imageSrc,setImageSrc] = useState(null);
    const [imgName,setImgName] = useState('')

    const check = async ()=>{
        const formData = new FormData();
        formData.append('imageFile', imageSrc);

        const response = await axios.post("http://127.0.0.1:5002/get-image",formData)
        
        setImgName(response.data.prediction)
    }


  const handleImageChange = (e) => {
    const selectedFile = e.target.files[0];
    
    if (selectedFile && selectedFile.type.startsWith('image/')) {
        setImageSrc(selectedFile);
    } else {
      alert('Please select a valid image file.');
        setImageSrc(null);
    }
  };

    return (
        <div className="hello">
            <div>{imageSrc ? <img src={URL.createObjectURL(imageSrc)} alt="Image" />: <>not found</> }</div>
            <div>
                <input type="file" accept="image/*" onChange={(e) => handleImageChange(e)}></input>
            </div>
            <div>
                <button onClick={()=> check()}>Check the image</button>
            </div>
            <div>
                <h3>Prediction is : {imgName}</h3>
            </div>
        </div>
    )
}

export default Image;