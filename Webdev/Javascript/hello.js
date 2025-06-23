const mstr =
  "Riya F 12-03-2004.Ajay M 25-07-2003.Neha F 09-11-2005.Sahil M 30-01-2002.Anita F 18-06-2006.Karan M 14-08-2001.Meera F 22-12-2004.Rohan M 03-05-2003.Sana F 27-09-2005.Vikram M 11-02-2002.Kavya F 05-07-2006.Tarun M 19-10-2003.Isha F 15-03-2004.Aryan M 08-06-2002.Nidhi F 24-01-2005.Yash M 02-04-2003.Pooja F 17-12-2004.Arjun M 10-09-2002.Simran F 28-11-2005.Dev M 13-02-2001.Maya F 06-08-2004.Harsh M 21-03-2002.Alia F 01-05-2006.Manish M 16-07-2003.Shruti F 29-10-2004.Aditi F 19-04-2002.Rahul M 07-11-2005.Priya F 23-02-2003.Sumit M 12-09-2001.Anjali F 04-01-2006.Deepak M 26-06-2004.Kriti F 11-10-2002.Mohit M 09-03-2005.Sonam F 14-07-2003.Amit M 20-12-2001.Juhi F 03-08-2006.Varun M 18-05-2004.Diya F 25-09-2002.Raj M 02-02-2005.Tanya F 30-07-2003.Gaurav M 17-11-2001.Parul F 08-04-2006.Nikhil M 22-08-2004.Chhavi F 13-01-2002.Ankit M 28-05-2005.Ishita F 10-10-2003.Sahil M 05-03-2001.Sneha F 24-06-2006.Abhishek M 15-09-2004.Muskan F 27-02-2002.Vivek M 14-11-2005.Aisha F 19-08-2003.Rohit M 01-01-2001.Divya F 29-04-2006.Ankur M 16-12-2004.Shreya F 06-07-2002.Aditya M 23-10-2005.Palak F 11-05-2003.Vikas M 04-09-2001.Esha F 20-02-2006.Pranav M 09-12-2004.Ritu F 07-06-2002.Sameer M 26-11-2005.Heena F 12-04-2003.Kunal M 31-08-2001.Jhanvi F 18-01-2006.Mohan M 21-07-2004.Geeta F 02-10-2002.Aarav M 20-08-2005.";

const gen = "m";

const minage = 21;

var arr;

if (gen == "m" || gen == "M") {
  arr = mstr.match(/\b([a-zA-z]+) ([mM]) (\d{2})-(\d{2})-(\d{4})/g);
} else if (gen == "f" || gen == "F") {
  arr = mstr.match(/\b([a-zA-z]+) ([fF]) (\d{2})-(\d{2})-(\d{4})/g);
} else if (gen == "A" || gen == "a") {
  arr = mstr.match(/\b([a-zA-z]+) ([MmFf]) (\d{2})-(\d{2})-(\d{4})/g);
}

console.log("The Filtered People Are-\n");

function chkage(ar) {
  let ag = new Date(ar);
  let var1 = ag.getTime();
  let n = new Date();
  let var2 = n.getTime();
  let numili = minage * 365 * 24 * 60 * 60 * 1000;
  let finage = var2 - var1;

  return finage >= numili ? true : false;
}

for (const entr of arr) {
  const arr2 = entr.match(/(\d{2})-(\d{2})-(\d{4})/);
  var sf = arr2[0];
  if (chkage(sf) == true) {
    console.log(entr);
  }
}
