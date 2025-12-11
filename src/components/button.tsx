'use client';
import { useRef } from 'react';
import { ChangeEvent } from 'react';
import { useState } from 'react';

export default function Button() {
  const [errorMessage, setErrorMessage] = useState('');
  const uploadRef = useRef<HTMLInputElement>(null);
  const allowedTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
  let handleClick = () => {
    uploadRef.current?.click();
  }
  let  handleUpload = async (event: ChangeEvent<HTMLInputElement> ) => {

   if (event.target.files == null) {
      console.log("File was unsuccessful");
      return
   }
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append("resume",file);
    if (allowedTypes.includes(file.type)){
      try{ 
        const response = await fetch('http://localhost:5000/upload', {method: "POST", body: formData })
        
      }
      catch (error)
      {
        console.error("Error:", error);
      }
    }
    else{
      setErrorMessage('This file type is not supported.')
    }
  }


  return (
    <>
      <button onClick={handleClick}> Upload File</button>
      <input type="file" accept=".docx, .pdf, .txt" style={{ display: 'none' }}  onChange={handleUpload} ref={uploadRef} ></input>
      {errorMessage ? <p> {errorMessage}</p> : null }
    </>

  )
}