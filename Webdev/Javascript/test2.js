try {
  console.log("try statement\n");
  throw "bullshit error\n";
} catch (e) {
  console.log(e);
  return true;
} finally {
  console.log("finally this\n");
  return false;
}
