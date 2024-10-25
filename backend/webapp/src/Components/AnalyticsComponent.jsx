import React from "react";
import LineGraph from "./LineGraph";
import { Accordion } from "react-bootstrap";

const AnalyticsComponent = ({ biometrics }) => {
  const categorizeBiometrics = () => {
    const hypo = [];
    const hyper = [];
    const normal = [];

    for (const bio of biometrics) {
      for (const [name, data] of Object.entries(bio)) {
        const sortedValues = data.values
          .slice()
          .sort((a, b) => new Date(a.created) - new Date(b.created));
        const latestValue = sortedValues[sortedValues.length - 1].scaled_value;

        if (latestValue < -1) {
          hypo.push({ [name]: data });
        } else if (latestValue > 1) {
          hyper.push({ [name]: data });
        } else {
          normal.push({ [name]: data });
        }
      }
    }

    return { hypo, hyper, normal };
  };

  const { hypo, hyper } = categorizeBiometrics();

  const renderBiochemicals = (biochemicals, title) => (
    <div className=" mb-3" style={{ width: "100%" }}>
      <h6 className="w-100 mt-3 text-center">{title}</h6>
      <div style={{ overflowY: "auto", maxHeight: "100%", padding: "10px" }}>
        {biochemicals.map((item, index) => (
          <div key={index} className="mb-2 w-100">
            <LineGraph data={item} />
          </div>
        ))}
      </div>
    </div>
  );

  const categorizedBiometrics = biometrics.reduce((acc, metric) => {
    const key = Object.keys(metric)[0];
    const category = metric[key].category;

    if (!acc[category]) {
      acc[category] = [];
    }
    acc[category].push(metric);
    return acc;
  }, {});

  return (
    <div className="w-100 h-100 d-flex">
      {/* Left Column with Scroll */}
      <div
        className=" d-flex flex-column align-items-center justify-content-start"
        style={{ width: "50%", height: "100%", overflowY: "auto" }}
      >
        {/* Hyper Biochemicals */}
        {renderBiochemicals(hyper, "Hyper Biochemicals")}

        {/* Hypo Biochemicals */}
        {renderBiochemicals(hypo, "Hypo Biochemicals")}
      </div>

      {/* Right Section (fixed height, no scroll) */}
      <div
        className=" d-flex align-items-center justify-content-center p-3"
        style={{ width: "50%", height: "100%", overflow: "auto" }}
      >
        <Accordion className="w-100 h-100 border-none" >
          {Object.keys(categorizedBiometrics).map((category, index) => (
            <Accordion.Item className="border-none" eventKey={index.toString()} key={index}>
              <Accordion.Header>
                <strong>{category}</strong>
              </Accordion.Header>
              <Accordion.Body>
                {categorizedBiometrics[category].map((metric, i) => {
                  const key = Object.keys(metric)[0];
                  const lastValue =
                    metric[key].values[metric[key].values.length - 1];
                  const isExpired =
                    new Date(lastValue.expired_date) < new Date();

                  return (
                    <div key={i} style={{ marginBottom: "20px" }}>
                      <strong>
                        {key}{" "}
                        {isExpired && (
                          <span style={{ color: "red" }}>
                            *Expired on{" "}
                            {new Date(
                              lastValue.expired_date
                            ).toLocaleDateString("en-GB")}
                          </span>
                        )}
                      </strong>
                      <LineGraph data={metric} />
                    </div>
                  );
                })}
              </Accordion.Body>
            </Accordion.Item>
          ))}
        </Accordion>
      </div>
    </div>
  );
};


export default AnalyticsComponent;
