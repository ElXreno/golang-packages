%global goipath         gitlab.com/strk/go-libravatar
%global commit          5eed7bff870ae19ef51c5773dbc8f3e9fcbd0982
%global scm             git

%gometa

%global common_description %{expand:
Simple golang library for serving federated avatars.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Simple golang library for serving federated avatars.

License:                Custom
URL:                    %{gourl}
Source0:                %{gosource}

Provides:               golang(strk.kbt.io/projects/go/libravatar) = %{version}-%{release}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
