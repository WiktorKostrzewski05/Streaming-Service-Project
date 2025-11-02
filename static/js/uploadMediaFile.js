async function uploadFile(source, mediaId, mediaName) {

    const fileInput = document.getElementById('input-' + source + "-" + mediaId);
    const fileSuccessTest = document.getElementById("uploaded-" + source + "-" + mediaId)
    console.log(fileSuccessTest)
    const file = fileInput.files[0];
    const extension = file.name.split(".")

    let newPath = source + mediaName + mediaId + "." + extension[1]
    let dbField = "file_url"


    const supabaseClient = supabase.createClient('https://jyvpolkvpfnmjhejbszp.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp5dnBvbGt2cGZubWpoZWpic3pwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcwODE3NjgzOCwiZXhwIjoyMDIzNzUyODM4fQ.sFJTvmb6pGU_fTvIBTIYUgYwCh6q-aSGec8jGH1KhS8');
    console.log(supabaseClient)
    fileSuccessTest.className = "text-primary"
    fileSuccessTest.innerHTML = "Updating file..."
    let res = await supabaseClient.storage.from('Main').upload(newPath, file, { upsert: true });
    let publicUrl = await supabaseClient.storage.from('Main').getPublicUrl(newPath)

    publicUrl = publicUrl.data.publicUrl
    let resDB = await supabaseClient.from('mediaApp_mediafile').update({ [dbField]: publicUrl }).eq('id', mediaId)
    fileSuccessTest.className = "text-success"
    fileSuccessTest.innerHTML = "File Updated"

    console.log(res);

};