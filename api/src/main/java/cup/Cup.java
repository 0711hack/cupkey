package cup;

import com.fasterxml.jackson.annotation.JsonIgnore;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity // This tells Hibernate to make a table out of this class
public class Cup {
    @JsonIgnore
	@Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;
	private String certificateHash;
	private int claimingTimestamp;


	public String getCertificateHash() {
		return certificateHash;
	}

	public void setCertificateHash(String certificateHash) {
		this.certificateHash = certificateHash;
	}

	public int getClaimingTimestamp() {
		return claimingTimestamp;
	}

	public void setClaimingTimestamp(int claimingTimestamp) {
		this.claimingTimestamp = claimingTimestamp;
	}

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}
}

