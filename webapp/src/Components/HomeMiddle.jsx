import React from "react";
import { Card } from "react-bootstrap";
import LineGraph from "./LineGraph";
import { useUser } from "../Contexts/UserContext"; // Make sure useUser is imported
import SpinnerComponent from "./SpinnerComponent";

const HomeMiddle = ({ biometrics }) => {
  const { userLoading } = useUser();

  const categorizeBiometrics = () => {
    const hypo = [];
    const hyper = [];
    const normal = [];

    for (const bio of biometrics) {
      for (const [name, data] of Object.entries(bio)) {
        const sortedValues = data.values.slice().sort((a, b) => new Date(a.created) - new Date(b.created));
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
    <div className="card min-height-30px">
      <h5 className="p-3">{title}</h5>
      <div className="card-body p-0-2">
        <div className="row">
          {biochemicals.map((item, index) => (
            <div key={index} className="col-12 col-md-6 mb-2">
              <div className="border p-2">
                <LineGraph data={item} />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  return (
    <Card className="primary-card">
      <Card.Body className="d-flex flex-column gap-2">
        {userLoading ? (
          <SpinnerComponent/>
        ) : (
          biometrics.length === 0 ? (
            <span className="badge m-auto rounded-pill bg-secondary">
              Biometrics data not available
            </span>
          ) : (
            <>
              {hyper.length > 0 && renderBiochemicals(hyper, "Hyper Biochemicals")}
              {hypo.length > 0 && renderBiochemicals(hypo, "Hypo Biochemicals")}
            </>
          )
        )}
      </Card.Body>
    </Card>
  );
};

export default HomeMiddle;
