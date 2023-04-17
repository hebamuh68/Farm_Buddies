import "./Hero.css";

function Hero() {
  return (
    <>
      <div id="Hero_section" className="container">
        <div className="row">
          <div className="col-md-4">
            <img id="cat" alt="" src={require("../images/Hero/logoo.gif")} />
            <img id="paw1" alt="" src={require("../images/Hero/paw2.png")} />
          </div>
          <div className="col-md-4 title">
            <h1>Find</h1>
            <h2>Your study partner</h2>
          </div>
          <div className="col-md-4">
            <img id="paw2" alt="" src={require("../images/Hero/paw2.png")} />
          </div>
        </div>        
      </div>
    </>
  );
}

export default Hero;
